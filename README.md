# PDF-Doctor

Introduction:

The ability for patients to access and understand their medical records is an important part of healthcare empowerment. However, medical reports can often be dense and confusing for non-experts. Recent advances in natural language processing present an opportunity to bridge this gap. The PDF-Doctor application explored in this paper allows users to upload a PDF medical report, and ask natural language questions about its content. The system then provides clear explanations by retrieving relevant snippets from the report.  

Purpose:

The purpose of this project is to enable patients to gain a better understanding of their health by querying their medical reports. The PDF-Doctor application provides an intuitive interface for users to get answers to their questions. Under the hood, the system leverages state-of-the-art NLP techniques to parse medical reports and generate responses. The goal is to make medical information more accessible to patients.

Methodology:

The system workflow consists of several stages. First, the PDF report is converted to text using PdfPlumber. Next, sentence embeddings are generated using the pre-trained SentenceTransformers model. These embeddings allow semantically similar sentences to be matched, which is key for retrieval. The embeddings are indexed in a vector store using FAISS for efficient similarity search. User questions are likewise converted to embeddings. The vectors are fed into a Langchain retrieval pipeline, which matches questions to relevant report sentences. Finally, the retrieved snippets are provided as context to the Llama-2 conversational agent, which generates a natural language response.

Exploration:

Various tools and large language models were evaluated for each pipeline component. Initially, PyPDF2 was chosen for the pdf-to-text conversion process, but owing to the loss of structure when converting the PDFs to text files (pseudo-columns), the embeddings generated lost coherence. As a result, PdfPlumber was selected for its robustness in extracting text from PDFs, specifically for PDFs containing pseudo-structured elements. SentenceTransformers provides state-of-the-art performance on semantic similarity tasks and all-mini-lm-l6-v2 is five times as fast as the best-performing sentence transformers model while providing comparable performance. An exploration of BioClinical BERT (sentence transformer model fine-tuned on ICU data) was attempted, but the results generated, while highly accurate for embedding the medical information, were poor when considering conversational words and sentences. FAISS enables swift nearest neighbour lookup in the encoded vector space. Langchain offers a flexible framework for retrieval and chaining LLMs. Llama-2-7B-chat (8-bit quantized) generates high-quality conversational responses conditioned on context with a minimum overhead of 1 minute per user query owing to quantizing the inputs to 8-bit representations. This measure aids in decreasing latency while preserving necessary information. Together, these models provide an effective solution tailored for this medical query application. 

LLaMa-2 Exploration:

A.	Overview

Llama-2 is Meta's latest large language model, building on the success of the original Llama model. With up to 70 billion parameters, Llama-2 pushes the boundaries of model scale, while remaining accessible to researchers.

B.	Training and Reproducibility 

Like its predecessor, Llama-2 was trained on a huge dataset of text from diverse online sources. The multilingual training corpus focuses on high-resource languages using Latin and Cyrillic scripts. Llama-2's training regime optimizes for generative conversational applications. 

C.	Performance and Comparisons

Benchmark results demonstrate Llama-2's impressive capabilities. The 13B parameter model surpasses GPT-3 on many NLP tasks, despite being much smaller. Llama-2 also rivals top models like PaLM and Chinchilla, even outperforming them on certain datasets.

D.	Accessibility and Licensing

Llama-2 continues Meta's commitment to democratizing access to powerful models. Researchers can obtain Llama-2 for commercial use, enabling broad adoption and experimentation.

E.	Outcomes

Integrating Llama-2 into the talk-to-your-reports application generates responses to user queries with a high accuracy and relevance to the document with a minimal latency of 1 minute per query, all the while maintaining a conversational tone. Llama-2's responses are more concise yet comprehensive compared to prior models.

In summary, Llama-2 represents a leap forward in conversational AI. Its combination of cutting-edge performance and open availability makes it an exciting new asset for NLP research and applications. Llama-2 highlights Meta's role in pushing the boundaries of the language model scale while promoting open access.



Findings and Inference:

The exploration and implementation of various natural language processing tools and large language models yielded several key findings:
1.	PdfPlumber proved the most robust for extracting structured text from PDF medical reports, enabling higher-quality downstream embeddings. PyPDF2 was initially explored but did not reliably preserve the layout and pseudo-structured elements like columns.
2.	SentenceTransformers with the all-mini-lm-l6-v2 model provided efficient semantic similarity calculations for retrieval.
3.	Llama-2 demonstrated strong performance in generating conversational responses conditioned on retrieved medical report context.
4.	Quantizing Llama-2 inputs to 8-bits accelerated query response time to under 1 minute without losing critical information.
5.	BioClinicalBERT did not sufficiently capture conversational patterns despite medical domain tuning.

Decision-Making Process:

The model selection and implementation decisions balanced various factors:
1.	Accuracy in parsing key information from medical PDF reports was prioritized in the PDF conversion component.
2.	Speed, scalability and cost were optimized by choosing smaller high-performing models like all-mini-lm-l6-v2 and the 7B Llama-2 version.
3.	Conversational ability was maximized through Llama-2 fine-tuned on dialogue data, even with quantization tradeoffs.
4.	Ease of access to state-of-the-art models like Llama-2 enabled rapid experimentation.
5.	Infrastructure decisions focused on scalable, robust, cloud-based deployment.


Limitations and Challenges:

While substantial progress was made in evaluating and implementing large language models for medical query answering, some key challenges remain:

1.	Lack of abundant in-domain data - More comprehensive medical question datasets (medical report dataset) would improve model comprehension and accuracy and would aid in fine-tuning the Llama-2 model to better answer the queries from the reports. Crowd-sourcing real patient questions could be highly valuable.
2.	Insufficient compute for robust fine-tuning - Larger, specialized cloud compute instances would enable more thorough fine-tuning with longer training times and bigger batches.
3.	Engineering overhead - Significant effort was required for infrastructure setup, integration, and monitoring. Further automation and streamlining of the pipeline would increase efficiency.
4.	Ongoing maintenance - Continuous model evaluation and re-training will be needed to improve performance over time as new data emerges. Dedicated resources are required.

Future Directions:

There are several promising directions for future work. The system could be enhanced to handle other medical file formats beyond PDF, such as medical images or doctor's notes. More advanced LLMs such as Llama-2’s 13B and 70B parameter models could help generate improved answers. Personalization could be incorporated to adapt answers to the user's level of medical knowledge. The interface could be integrated with popular patient health portals for seamless access. As LLMs continue to advance, this application has much room for growth in capabilities.

Conclusion:

This application demonstrates how modern NLP techniques can empower patients with easy access to their medical records. Converting reports to text, generating semantic embeddings, efficient vector search, chained language models, and conversational response generation together enable a robust medical information retrieval and explanation system. There is ample opportunity to build on this foundation as LLMs evolve. By making medical knowledge more accessible, we can achieve better health outcomes.

