from rdflib import Graph, plugin
from rdflib.parser import Parser
from rdflib import URIRef, Literal, Graph, RDF, Namespace



# Set the paths to your CSV file and the ontology file
csv_file = "lianas.csv"  # Replace with the data source 
ontology_file = "foo.ttl" # Replace with the ontology

# Create an RDF graph
graph = Graph()

# Load the ontology into the graph
graph.parse(source=ontology_file, format="ttl")

# Set the namespace for your ontology
namespace = Namespace("https://w3id.org/def/foo#")
namespace1 = Namespace("http://www.w3.org/ns/sosa/")

# RML mapping code
# Iterate over the CSV file and map the data to RDF triples
with open(csv_file, 'r') as file:
    # Skip the header row if present
    next(file)

    for line in file:
        # Split the CSV line into columns
        columns = line.strip().split(',')

        # Extract column values (modify as per your CSV structure)
        column1 = columns[0]
        column2 = columns[1]
        column3 = columns[2]
        column4 = columns[3]
        column5 = columns[4]
        column6 = columns[5]
        column7 = columns[6]
        column8 = columns[7]
        column9 = columns[8]
        column10 = columns[9]
        column11 = columns[10]
        column12 = columns[11]
        
        

        # Create subject URI
        subject_uri = URIRef(namespace + column1)

        # Add triples to the graph
        graph.add((subject_uri, RDF.type, namespace1.Observation))  # Replace with the appropriate class from your ontology
        graph.add((subject_uri, namespace.Plot_no, Literal(column2)))  # Replace with the appropriate predicate from your ontology
        graph.add((subject_uri, namespace.Site_plot_code, Literal(column3)))
        graph.add((subject_uri, namespace.Date, Literal(column4)))
        graph.add((subject_uri, namespace.Tree_individual_no, Literal(column5)))
        graph.add((subject_uri, namespace.Tree_ID, Literal(column6)))
        graph.add((subject_uri, namespace.Tree_dbh_cm, Literal(column7)))
        graph.add((subject_uri, namespace.Tree_height_m, Literal(column8)))
        graph.add((subject_uri, namespace.Tree_N_lianas, Literal(column9)))
        graph.add((subject_uri, namespace.Liana_dbh_cm, Literal(column10)))
        graph.add((subject_uri, namespace.Tree_notes, Literal(column11)))
        graph.add((subject_uri, namespace.Subplot_radius_m, Literal(column12)))
      

# Save the resulting knowledge graph to a file
output_file = "VegKG.rdf"
graph.serialize(destination=output_file, format= "xml")


