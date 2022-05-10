# A ETL pipeline using [prefect](https://www.prefect.io/)

This repository contains ETL pipeline for https://osti.gov/ .

## Running data pipeline

1. Clone repo: <code> https://github.com/pradipthapa7374/prefect_etl_pipeline</code>
2. cd prefect_etl_pipeline
3. <code> pip install -r requirements.txt </code>
4. Setup prefect cloud backend: <code>prefect backend cloud</code>
5. Authenticate with Prefect Cloud: <code> prefect auth login --key YOUR-KEY </code> API key can be created by signing up at https://cloud.prefect.io/user/keys
6. Once authenticated run prefect UI on the cloud.


## Output
1. Running the flow creates osti_data.db which stores scraped data in the form of (id, title, url) as column names.
2. osti_data.json which is loaded to the elasticsearch as well as saved as local files.
    ```
    [
    {
        "osti_id": "1856447",
        "title": "Static quark-antiquark interactions at nonzero temperature from lattice QCD",
        "author_details": [
            "{\"role\":\"\",\"contributor_type\":\"\",\"affiliation\":\"\",\"last_name\":\"Bala\",\"orcid\":\"\",\"middle_name\":\"\",\"first_name\":\"Dibyendu\"}",
            "{\"role\":\"\",\"contributor_type\":\"\",\"affiliation\":\"\",\"last_name\":\"Kaczmarek\",\"orcid\":\"\",\"middle_name\":\"\",\"first_name\":\"Olaf\"}",
            "{\"role\":\"\",\"contributor_type\":\"\",\"affiliation\":\"\",\"last_name\":\"Larsen\",\"orcid\":\"\",\"middle_name\":\"\",\"first_name\":\"Rasmus\"}",
            "{\"role\":\"\",\"contributor_type\":\"\",\"affiliation\":\"\",\"last_name\":\"Mukherjee\",\"orcid\":\"\",\"middle_name\":\"\",\"first_name\":\"Swagato\"}",
            "{\"role\":\"\",\"contributor_type\":\"\",\"affiliation\":\"\",\"last_name\":\"Parkar\",\"orcid\":\"\",\"middle_name\":\"\",\"first_name\":\"Gaurang\"}",
            "{\"role\":\"\",\"contributor_type\":\"\",\"affiliation\":\"\",\"last_name\":\"Petreczky\",\"orcid\":\"\",\"middle_name\":\"\",\"first_name\":\"Peter\"}",
            "{\"role\":\"\",\"contributor_type\":\"\",\"affiliation\":\"\",\"last_name\":\"Rothkopf\",\"orcid\":\"\",\"middle_name\":\"\",\"first_name\":\"Alexander\"}",
            "{\"role\":\"\",\"contributor_type\":\"\",\"affiliation\":\"\",\"last_name\":\"Weber\",\"orcid\":\"\",\"middle_name\":\"Heinrich\",\"first_name\":\"Johannes\"}"
        ],
        "report_number": "BNL-222900-2022-JAAM",
        "doi": "https://doi.org/10.1103/PhysRevD.105.054513",
        "product_type": "Journal Article",
        "language": "English",
        "country_publication": "United States",
        "description": "We study the interactions of a static quark antiquark pair at non-zero temperature using realistic 2+1 flavor lattice QCD calculations. The study consists of two parts: the first investigates the properties of Wilson line correlators in Coulomb gauge and compares to predictions of hard-thermal loop perturbation theory. As a second step we extract the spectral functions underlying the correlators using four conceptually different methods: spectral function fits, a HTL inspired fit for the correlation function, Pad\u00e9 rational approximation and the Bayesian BR spectral reconstruction. We find that our high statistics Euclidean lattice data are amenable to different hypotheses for the shapes of the spectral function and we compare the implications of each analysis method for the existence and properties of a well defined ground state spectral peak.",
        "publication_date": "2022-03-24T00:00:00Z",
        "entry_date": "2022-03-25T00:00:00Z",
        "publisher": "American Physical Society",
        "journal_name": "Physical Review D",
        "journal_issue": "5",
        "journal_volume": "105",
        "format": "Medium: X",
        "authors": [
            "Bala, Dibyendu",
            "Kaczmarek, Olaf",
            "Larsen, Rasmus",
            "Mukherjee, Swagato",
            "Parkar, Gaurang",
            "Petreczky, Peter",
            "Rothkopf, Alexander",
            "Weber, Johannes Heinrich",
            "HotQCD Collaboration"
        ],
        "subjects": [
            "73 NUCLEAR PHYSICS AND RADIATION PHYSICS",
            "color confinement",
            "finite temperature field theory",
            "heavy quark effective theory",
            "lattice QCD",
            "lattice field theory",
            "quark-gluon plasma",
            "Bayesian methods"
        ],
        "article_type": "Published Article",
        "contributing_org": "HotQCD Collaboration",
        "doe_contract_number": "SC0012704; AC05- 00OR22725; AC02- 05CH11231; 286883; NN9578K-QCDrtX; AC05-00OR22725; AC02-05CH11231",
        "sponsor_orgs": [
            "USDOE Office of Science (SC), Nuclear Physics (NP)",
            "Research Council of Norway",
            "German Research Foundation (DFG)"
        ],
        "research_orgs": [
            "Brookhaven National Lab. (BNL), Upton, NY (United States)",
            "Oak Ridge National Lab. (ORNL), Oak Ridge, TN (United States)",
            "Lawrence Berkeley National Lab. (LBNL), Berkeley, CA (United States)"
        ],
        "journal_issn": "ISSN 2470-0010",
        "other_identifiers": [
            "Journal ID: ISSN 2470-0010; PRVDAQ;  054513"
        ],
        "links": [
            {
                "rel": "citation",
                "href": "https://www.osti.gov/biblio/1856447"
            }
        ]
    },
    {
        "osti_id": "1830237",
        "title": "Sulfate adenylyl transferase kinetics and mechanisms of metabolic inhibitors of microbial sulfate respiration",
        "author_details": [
            "{\"role\":\"\",\"contributor_type\":\"\",\"affiliation\":\"\",\"last_name\":\"Carlson\",\"orcid\":\"0000000215835313\",\"middle_name\":\"K.\",\"first_name\":\"Hans\"}",
            "{\"role\":\"\",\"contributor_type\":\"\",\"affiliation\":\"\",\"last_name\":\"Youngblut\",\"orcid\":\"\",\"middle_name\":\"D.\",\"first_name\":\"Matthew\"}",
            "{\"role\":\"\",\"contributor_type\":\"\",\"affiliation\":\"\",\"last_name\":\"Redford\",\"orcid\":\"0000000311499401\",\"middle_name\":\"A.\",\"first_name\":\"Steven\"}",
            "{\"role\":\"\",\"contributor_type\":\"\",\"affiliation\":\"\",\"last_name\":\"Williamson\",\"orcid\":\"\",\"middle_name\":\"J.\",\"first_name\":\"Adam\"}",
            "{\"role\":\"\",\"contributor_type\":\"\",\"affiliation\":\"\",\"last_name\":\"Coates\",\"orcid\":\"000000021631734X\",\"middle_name\":\"D.\",\"first_name\":\"John\"}"
        ],
        "doi": "https://doi.org/10.1038/s43705-021-00069-1",
        "product_type": "Journal Article",
        "language": "English",
        "country_publication": "Country unknown/Code not available",
        "description": "<title>Abstract</title>\n <p>\n Sulfate analog oxyanions that function as selective metabolic inhibitors of dissimilatory sulfate reducing microorganisms (SRM) are widely used in ecological studies and industrial applications. As such, it is important to understand the mode of action and mechanisms of tolerance or adaptation to these compounds. Different oxyanions vary widely in their inhibitory potency and mechanism of inhibition, but current evidence suggests that the sulfate adenylyl transferase/ATP sulfurylase (Sat) enzyme is an important target. We heterologously expressed and purified the Sat from the model SRM,\n <italic>Desulfovibrio alaskensis</italic>\n G20. With this enzyme we determined the turnover kinetics (\n <italic>k</italic>\n <sub>cat</sub>\n ,\n <italic>K</italic>\n <sub>M</sub>\n ) for alternative substrates (molybdate, selenate, arsenate, monofluorophosphate, and chromate) and inhibition constants (\n <italic>K</italic>\n <sub>I</sub>\n ) for competitive inhibitors (perchlorate, chlorate, and nitrate). These measurements enable the first quantitative comparisons of these compounds as substrates or inhibitors of a purified Sat from a respiratory sulfate reducer. We compare predicted half-maximal inhibitory concentrations (IC\n <sub>50</sub>\n ) based on Sat kinetics with measured IC\n <sub>50</sub>\n values against\n <italic>D. alaskensis</italic>\n G20 growth and discuss our results in light of known mechanisms of sensitivity or resistance to oxyanions. This analysis helps with the interpretation of recent adaptive laboratory evolution studies and illustrates the value of interpreting gene\u2013microbe\u2013environment interactions through the lens of enzyme kinetics.\n </p>",
        "publication_date": "2021-11-13T00:00:00Z",
        "entry_date": "2021-11-16T00:00:00Z",
        "publisher": "Nature Publishing Group",
        "journal_name": "ISME Communications",
        "journal_issue": "1",
        "journal_volume": "1",
        "format": "Medium: X",
        "authors": [
            "Carlson, Hans K. (ORCID:0000000215835313)",
            "Youngblut, Matthew D.",
            "Redford, Steven A. (ORCID:0000000311499401)",
            "Williamson, Adam J.",
            "Coates, John D. (ORCID:000000021631734X)"
        ],
        "article_type": "Published Article",
        "doe_contract_number": "AC02-05CH11231",
        "subjects": [],
        "sponsor_orgs": [
            "USDOE"
        ],
        "research_orgs": [],
        "journal_issn": "ISSN 2730-6151",
        "other_identifiers": [
            "Journal ID: ISSN 2730-6151;  67; PII: 69"
        ],
        "links": [
            {
                "rel": "citation",
                "href": "https://www.osti.gov/biblio/1830237"
            }
        ]
    },
    {
        "osti_id": "1845028",
        "title": "Distinctive carbon repression effects in the carbohydrate-selective wood decay fungus Rhodonia placenta",
        "author_details": [
            "{\"role\":\"\",\"contributor_type\":\"\",\"affiliation\":\"\",\"last_name\":\"Zhang\",\"orcid\":\"\",\"middle_name\":\"\",\"first_name\":\"Jiwei\"}",
            "{\"role\":\"\",\"contributor_type\":\"\",\"affiliation\":\"\",\"last_name\":\"Meng Markillie\",\"orcid\":\"\",\"middle_name\":\"\",\"first_name\":\"Lye\"}",
            "{\"role\":\"\",\"contributor_type\":\"\",\"affiliation\":\"\",\"last_name\":\"Mitchell\",\"orcid\":\"0000000301438461\",\"middle_name\":\"D.\",\"first_name\":\"Hugh\"}",
            "{\"role\":\"\",\"contributor_type\":\"\",\"affiliation\":\"\",\"last_name\":\"Gaffrey\",\"orcid\":\"\",\"middle_name\":\"J.\",\"first_name\":\"Matthew\"}",
            "{\"role\":\"\",\"contributor_type\":\"\",\"affiliation\":\"\",\"last_name\":\"Orr\",\"orcid\":\"\",\"middle_name\":\"\",\"first_name\":\"Galya\"}",
            "{\"role\":\"\",\"contributor_type\":\"\",\"affiliation\":\"\",\"last_name\":\"Schilling\",\"orcid\":\"\",\"middle_name\":\"S.\",\"first_name\":\"Jonathan\"}"
        ],
        "report_number": "PNNL-SA-170453",
        "doi": "https://doi.org/10.1016/j.fgb.2022.103673",
        "product_type": "Journal Article",
        "language": "English",
        "country_publication": "United States",
        "description": "Brown rot fungi dominate the carbon degradation of northern terrestrial conifers. These fungi adapted unique genetic inventories to degrade lignocellulose and to rapidly release a large quantity of carbohydrates for fungal catabolism. We know that brown rot involves \u201ctwo-step\u201d gene regulation to delay most hydrolytic enzyme expression until after harsh oxidative pretreatments. This implies the crucial role of concise gene regulation to brown rot efficacy, but the underlying regulatory mechanisms remain uncharacterized. Here, using the combined transcriptomic and enzyme analyses we investigated the roles of carbon catabolites in controlling gene expression in model brown rot fungus Rhodonia placenta. We identified co-regulated gene regulons as shared transcriptional responses to no-carbon controls, glucose, cellobiose, or aspen wood (Populus sp.). We found that cellobiose, a common inducing catabolite for fungi, induced expression of main chain-cleaving cellulases in GH5 and GH12 families (cellobiose vs. no-carbon > 4-fold, Padj < 0.05), whereas complex aspen was a universal inducer for Carbohydrate Active Enzymes (CAZymes) expression. Importantly, we observed the attenuated glucose-mediated repression effects on cellulases expression, but not on hemicellulases and lignin oxidoreductases, suggesting fungi might have adapted diverged regulatory routes to boost cellulase production for the fast carbohydrate release. Using carbon regulons, we further predicted the cis- and trans-regulatory elements and assembled a network model of the distinctive regulatory machinery of brown rot. These results offer mechanistic insights into the energy efficiency traits of a common group of decomposer fungi with enormous influence on the carbon cycle.",
        "publication_date": "2022-04-01T00:00:00Z",
        "entry_date": "2022-02-24T00:00:00Z",
        "publisher": "Elsevier",
        "journal_name": "Fungal Genetics and Biology",
        "journal_issue": "C",
        "journal_volume": "159",
        "format": "Medium: X; Size: Article No. 103673",
        "authors": [
            "Zhang, Jiwei",
            "Meng Markillie, Lye",
            "Mitchell, Hugh D. (ORCID:0000000301438461)",
            "Gaffrey, Matthew J.",
            "Orr, Galya",
            "Schilling, Jonathan S."
        ],
        "subjects": [
            "brown rot",
            "fungal decomposer",
            "glucose repression",
            "gene expression",
            "regulatory network",
            "fungal trait"
        ],
        "article_type": "Published Article",
        "doe_contract_number": "AC05-76RL01830; SC0022151; SC001947",
        "sponsor_orgs": [
            "USDOE Office of Science (SC), Biological and Environmental Research (BER)"
        ],
        "research_orgs": [
            "Pacific Northwest National Lab. (PNNL), Richland, WA (United States)"
        ],
        "journal_issn": "ISSN 1087-1845",
        "other_identifiers": [
            "Journal ID: ISSN 1087-1845;  S1087184522000172; 103673; PII: S1087184522000172"
        ],
        "links": [
            {
                "rel": "citation",
                "href": "https://www.osti.gov/biblio/1845028"
            }
        ]
    }
    ]
    ```
3. all ids with given query which is loaded to the elasticsearch as well as saved as local files.
```
   {
    "G20": [
        "1856447",
        "1830237",
        "1845028",
        "1832807",
        "1855822",
        "1855786",
        "1847876",
        "1854910",
        "1830070",
        "1837374",
        "1838498",
        "1845007",
        "1822521",
        "1854582",
        "1829463",
        "1863940",
        "1841465",
        "1818675",
        "1823534",
        "1822783"
    ]
}
```


## Running on docker (Partial)
1. To run prefect on Docker, write a Dockerfile containing following components:
    - FROM: base image that we will be using for our image
    - WORKDIR: setting working directory for the container
    - ADD: add all of our files from the current directory to the container WORKDIR
    - RUN: install our library . This will also install all requirements.

2. Building an image:
<code>docker build . -t test:latest</code>

3. After creating image push to registry (using DockerHub)