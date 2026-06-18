# MODEL CARD

## System Purpose

Sahaha answers public-service questions for Saha-gu Office using official web content and a retrieval-augmented generation pipeline.

## Models Used

- Generation model: Groq-hosted `llama-3.3-70b-versatile`
- Embedding model: `sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2`
- NER model for privacy masking: `Leo97/KoELECTRA-small-v3-modu-ner`

## Data Sources

- Official Saha-gu website pages
- Official Saha-gu staff directory:
  `https://www.saha.go.kr/portal/staff/list.do?mId=0604030000`

## Intended Use

- Public information guidance
- Department routing
- Contact lookup
- Civil-service information explanation

## Out Of Scope

- Legal advice
- Medical diagnosis
- Open-ended factual answers outside official Saha-gu sources
- Processing of personal or sensitive user data

## Safety Measures

- Front-end privacy-input blocking
- Back-end personal-information masking
- Official-source-only retrieval grounding
- Contact enforcement from the official staff directory

## Known Limitations

- Quality depends on the freshness of crawled official data
- Some answers may require manual verification when the source site changes structure
- Full production deployment still depends on external secret configuration
