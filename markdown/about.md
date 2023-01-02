# About

*VulgateAI* is a new tool that allows users to query the Latin Vulgate (Clementine version) leveraging artificial intelligence, specifically machine learning. All approximate 35k lines of scripture were vectorized with the [Vulgata-spaCy](https://github.com/wjbmattingly/vulgata-spacy) pipeline which was specifically trained on the entire Patrologia Latina to ensure that the embeddings would match well both Scripture and medieval Latin. These embeddings allow the tool to capture semantic and syntactic meaning, not just perform a naive fuzzy word search.

Each line and its components (phrases found within each verse) were then mapped to an [Annoy index](https://github.com/spotify/annoy). Due to the complexity of the problem, 400 trees were necessary to ensure quality matches balanced against disk space. When a user enters a phrase to query, their search is vectorized with the same pipeline and that embedding is then matched to the annoy Index.

# How to Use the Tool
To use *VulgateAI*, simply paste a line from a text that you think may be rooted in Scripture. *VulgateAI* will return the potential candidates for a match.

Users can choose how many results to display with 'Max Results' and also the way in which the data is displayed with 'Display Style'. While a 'Table' will be easier to read, the 'DataFrame' is indexed so that the columns can be sorted like an Excel Spreadsheet.
