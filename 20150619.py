from timeit import default_timer
# print (default_timer()-default_timer())/2
#
# raise SystemError(0)

from functions import *
mutation_type_title,mutation_type_data=import_file("/Users/radhikarawat/Downloads/mutation_type_ensemble.txt","\t",condition_value="splice", condition_index=8, operator="in", columns=[2,8])#, length=20000)
# #['Ensembl Gene ID', 'Ensembl Transcript ID', 'Variant Name', 'Variant supporting evidence', 'Variant Chromosome Strand', 'Chromosome position start (bp)', 'Chromosome position end (bp)', 'Consequence specific allele', 'Variant Consequence', 'Variant Alleles', 'Associated Gene Name']

cosmic_mutant_title,cosmic_mutant_data=import_file("/Users/radhikarawat/Desktop/Programming/TCGA_projects/CosmicMutantExport.tsv","\t", columns=[16,23,24],condition_index=23,condition_value=":", operator="in", length=2000000)
#need this to get the chromosome #
# #Gene name	Accession Number	Gene CDS length	HGNC ID	Sample name	ID_sample	ID_tumour	Primary site	Site subtype 1	Site subtype 2	Site subtype 3	Primary histology	Histology subtype 1	Histology subtype 2	Histology subtype 3	Genome-wide screen	Mutation ID	Mutation CDS	Mutation AA	Mutation Description	Mutation zygosity	LOH	GRCh	Mutation genome position	Mutation strand	SNP	Resistance Mutation	FATHMM prediction	FATHMM score	Mutation somatic status	Pubmed_PMID	ID_STUDY	Sample source	Tumour origin	Age



sample_title,sample_data=import_file("/Users/radhikarawat/Desktop/Programming/TCGA_projects/tumor_sample_info.txt", "\t",columns=[4,5,6,7,15])
#['Hugo_Symbol', 'Entrez_Gene_Id', 'Center', 'Ncbi_Build', 'Chrom', 'Start_Position', 'End_Position', 'Strand', 'Variant_Classification', 'Variant_Type', 'Reference_Allele', 'Tumor_Seq_Allele1', 'Tumor_Seq_Allele2', 'Dbsnp_Rs', 'Dbsnp_Val_Status', 'Tumor_Sample_Barcode', 'Matched_Norm_Sample_Barcode', 'Match_Norm_Seq_Allele1', 'Match_Norm_Seq_Allele2', 'Tumor_Validation_Allele1', 'Tumor_Validation_Allele2', 'Match_Norm_Validation_Allele1', 'Match_Norm_Validation_Allele2', 'Verification_Status', 'Validation_Status', 'Mutation_Status', 'Sequencing_Phase', 'Sequence_Source', 'Validation_Method', 'Score', 'Bam_File', 'Sequencer', 'Tumor_Sample_UUID', 'Matched_Norm_Sample_UUID', 'File_Name', 'Archive_Name', 'Line_Number']


start_time=datetime.now()
start_timer=default_timer()
mutants=[]


IDs=[]
i=0
length=len(mutation_type_data)

for mutation in mutation_type_data:
    i+=1
    cosmicID = mutation[0]

    for cosmic_mutant in cosmic_mutant_data:
        if cosmicID==cosmic_mutant[0]:
            if 'splice' not in str(cosmic_mutant):
                if cosmicID not in IDs:
                    cosmic_mutant.append(mutation[1])
                    mutants.append(cosmic_mutant)
                    print i, length, datetime.now(), start_time, cosmic_mutant
f=open("mutants.txt","w+")
f.write(str(mutants))
f.close()
print 'cosmic mutant data length:', len(cosmic_mutant_data)
print 'mutants length:', len(mutants)
print 'elapsed time:', datetime.now()-start_time





start_time=datetime.now()
f=open("samples_matched_with_mutants.txt","w+")
i=0
length=len(sample_data)
for sample in sample_data:
    #print "progress:", i, length  # , datetime.now() - start_time
    i += 1
    sample_chromosome, sample_start, sample_end, sample_strand = sample[0:4]
    for mutant in mutants:
        start,end=mutant[1].split("-")
        chromosome,start=start.split(":")
        strand=mutant[2]

        if [chromosome, start, end, strand] == sample[0:4]:
            print "YES"
            line=str(mutant[0])+str(chromosome)+str(start)+str(end)+str(strand)+str(sample[5])+'\n'
            print "match", line
            #sample.append(mutant[0])
            #need to write: COSMID, Chromosome, start, end, strand, sampleID(15)
            f.write(line)

f.close()
