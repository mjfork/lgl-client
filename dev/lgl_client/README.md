Pulled the API defintion from https://api.littlegreenlight.com/api-docs/static.html

Converted it to markdown using https://urltomarkdown.com/ and saved it.

Copied and pasted the menu contents to get the sections & actions - these are essentially the classes and methods that need generated.

Used an LLM to generate a Python script to bring the big markdown file into the indivdiual files based on sections.

Used ChatGPT 4o with the following prompt to generate an o3 prompt to get SPEC.dm

```
Attached is the Little Green Light API definition and a prototype implementation I did for a handful of endpoints.  Your task is to write a ChatGPT o3 prompt to generate a technical specification in one shot that can be used by Claude Code to build the entire API Client out, section by section, testing and verifying after each piece.

Client should be written in python.  One model object produced for each entity that can be passed around (e.g. Gift, Constituent).  

The specification needs to be simple and concise.  No fluff.  

Ask all the questions you need to generate that high quality prompt.  Go.
```

