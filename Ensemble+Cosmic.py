#Annotates Ensemble and Cosmic data to form list of splice mutations, with cosmic IDs, chromosome, start, end, strand.
#e.g. ['COSM3875226', '6', '70475733', ;70475733', '+', 'splice_region_variant']


from functions import *

mutation_type_title,mutation_type_data=import_file("/Users/radhikarawat/Downloads/mutation_type_ensemble.txt","\t",condition_value="splice", condition_index=8, operator="in", columns=[2,8])
#['Ensembl Gene ID', 'Ensembl Transcript ID', 'Variant Name', 'Variant supporting evidence', 'Variant Chromosome Strand', 'Chromosome position start (bp)', 'Chromosome position end (bp)', 'Consequence specific allele', 'Variant Consequence', 'Variant Alleles', 'Associated Gene Name']


cosmic_mutant_title,cosmic_mutant_data=import_file("/Users/radhikarawat/Desktop/Programming/TCGA_projects/CosmicMutantExport.tsv","\t", columns=[16,23,24],condition_index=23,condition_value=":", operator="in", length=2000000)
#Gene name	Accession Number	Gene CDS length	HGNC ID	Sample name	ID_sample	ID_tumour	Primary site	Site subtype 1	Site subtype 2	Site subtype 3	Primary histology	Histology subtype 1	Histology subtype 2	Histology subtype 3	Genome-wide screen	Mutation ID	Mutation CDS	Mutation AA	Mutation Description	Mutation zygosity	LOH	GRCh	Mutation genome position	Mutation strand	SNP	Resistance Mutation	FATHMM prediction	FATHMM score	Mutation somatic status	Pubmed_PMID	ID_STUDY	Sample source	Tumour origin	Age

mutants=[]
IDs=[]
i=0
length=len(mutation_type_data)
for ensembl_mutant in mutation_type_data:
    i+=1
    cosmicID=ensembl_mutant[0]
    if cosmicID in IDs:
        print "duplicate"
        mutation_type_data=[x for x in mutation_type_data if x not in [ensembl_mutant]]
        mutation_type_data.remove(ensembl_mutant)
        print ensembl_mutant,"removed from mutation_type_data"
    elif cosmicID not in IDs:
        for cosmic_mutant in cosmic_mutant_data:
            cosmic_ID2=cosmic_mutant[0]
            if cosmic_ID2==cosmicID:
                cosmic_mutant_data = [x for x in cosmic_mutant_data if x not in [cosmic_mutant]]
                print cosmic_mutant, "removed from cosmic_mutant_data"
                IDs.append(cosmicID)
                cosmic_mutant.append(ensembl_mutant[1])
                mutants.append(cosmic_mutant)
                print cosmic_mutant, i, length


print mutants