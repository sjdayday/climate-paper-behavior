#!/usr/bin/env python3
"""Mechanical register pass (protocol v0.2 PC-9, exploratory).

Input: a JSON list of units {id, paper, side, author, lang, type, date, addressee, text}.
Output: per-unit CSV of hit counts by category, plus per-hit CSV with a first-pass target code.
Quoted material longer than 3 words is removed before counting (it is someone else's text).
Target code (first pass, to be audited): P = person (second person or named addressee in the
sentence), G = group (they/them/their or a collective noun in the sentence), W = work/argument.
"""
import json, re, sys, csv

LEX = json.load(open(sys.argv[1]))
units = json.load(open(sys.argv[2]))
out_units, out_hits = sys.argv[3], sys.argv[4]

QUOTE = re.compile(r'[“"„«‘]([^”"“»’]{0,2000})[”"“»’]')
def strip_quotes(t):
    return QUOTE.sub(lambda m: m.group(0) if len(m.group(1).split()) <= 3 else ' ', t)

GROUP = re.compile(r'\b(they|them|their|those|people|critics|skeptics|sceptics|modell?ers|the IPCC|IPCC|fact-?checkers?|climate scientists|warmists|alarmists|Skeptiker|Klimaskeptiker|die|diejenigen)\b', re.I)
SECOND = re.compile(r'\b(you|your|yourself|Sie|Ihr|Ihre|Ihnen|du|dein)\b')
CATS = ['R1_group_label','R2_competence','R3_motive_honesty','R4_ridicule_profanity','R5_exclusion_admonition']

def sentences(t):
    return re.split(r'(?<=[.!?])\s+|\n+', t)

rows, hits = [], []
for u in units:
    lang = u.get('lang','en'); lex = LEX[lang]
    t = strip_quotes(u['text'])
    words = len(re.findall(r'\w+', t))
    counts = {c:0 for c in CATS}
    seen_s = set()
    for s in sentences(t):
        if s.strip() in seen_s: continue
        seen_s.add(s.strip())
        for c in CATS:
            for pat in lex.get(c, []):
                for m in re.finditer(pat, s, re.I):
                    if c == 'R2_competence' and re.search(r'(know|understand)', m.group(0), re.I):
                        pre = s[:m.start()].strip().split()
                        if not pre or pre[-1].lower() in ('i','we','still','simply') and (len(pre)<2 or pre[-2].lower() in ('i','we')) or pre[-1].lower() in ('i','we'):
                            continue
                    counts[c] += 1
                    addr = (u.get('addressee') or '').split()
                    named = any(len(a) > 2 and re.search(r'\b'+re.escape(a)+r'\b', s) for a in addr)
                    tgt = 'P' if (SECOND.search(s) or named) else ('G' if GROUP.search(s) else 'W')
                    hits.append({'id':u['id'],'paper':u['paper'],'side':u['side'],'author':u['author'],
                                 'type':u['type'],'date':u['date'],'addressee':u.get('addressee',''),
                                 'category':c,'match':m.group(0),'target_firstpass':tgt,'sentence':s.strip()[:300]})
    r = {k:u.get(k,'') for k in ['id','paper','side','author','lang','type','date','addressee']}
    r.update(words=words, **counts, total=sum(counts.values()))
    rows.append(r)

with open(out_units,'w',newline='') as f:
    w = csv.DictWriter(f, fieldnames=list(rows[0].keys())); w.writeheader(); w.writerows(rows)
with open(out_hits,'w',newline='') as f:
    w = csv.DictWriter(f, fieldnames=list(hits[0].keys()) if hits else ['id']); w.writeheader(); w.writerows(hits)
print(f'{len(rows)} units, {len(hits)} hits')
