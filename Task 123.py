import networkx as nx
import matplotlib.pyplot as plt


# Task 1
goal_of_the_project="delivery of the project to the client"

results_list=["start of the project",
              "finishing the preparations",
              "finishing of the database",
              "finishing layout",
              "conceptual design",
              "preliminary design",
              "detailed design",
              "finishing testing",
              "upgrades",
              goal_of_the_project]
results_index= list(range(10))

work_list={
    "design_preparation" : 3,
    "database_design" : 4,
    "design_layout" : 1,
    "coding_dynamic_interface_elements" : 3,
    "preparation_of_the_website_texts" : 3,
    "coding_endpoints" : 3,
    "front_end_and_back_end_integration" : 2,
    "preparation_of_documents" : 2,
    "user_testing_the_website" : 3,
    "placement_of_documents_on_the_website" : 1,
    "payment_system_validation" : 3,
    "payment_system_integration" : 2,
}

print(f"Goal of the project: {goal_of_the_project}\n")

print(f"\nList of the results of the project:")

n=0

for i in results_list:
    print("    {}-{:40}".format(n,i))
    n+=1

print(f"\nList of work needed to finish the project:")

n=0

for i in work_list.keys():
    print("    {}-{:40}".format(n,i))
    n+=1

G = nx.Graph()

G.add_edges_from([(results_index[0], results_index[1]),
                  (results_index[0], results_index[2], ),
                  (results_index[1], results_index[3], ),
                  (results_index[3], results_index[4], ),
                  (results_index[1], results_index[4], ),
                  (results_index[2], results_index[4], ),
                  (results_index[4], results_index[5], ),
                  (results_index[3], results_index[6], ),
                  (results_index[6], results_index[7], ),
                  (results_index[5], results_index[7], ),
                  (results_index[6], results_index[7], ),
                  (results_index[7], results_index[8], ),
                  (results_index[8], results_index[9], ),
                            ])

nx.draw(G, with_labels = True)

plt.show()



# Task 2

dfs = nx.dfs_edges(G, source = results_index[0])

print ("DFS:", list(dfs))

bfs = nx.bfs_edges(G, source = results_index[0])

print ("BFS:", list(bfs))

#Task 3

for i, edge in enumerate(G.edges()):
    print(i, edge, work_list[list(work_list.keys())[i]])
    G[edge[0]][edge[1]]["weight"] = work_list[list(work_list.keys())[i]]

nx.draw(G, with_labels = True)
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos=nx.spring_layout(G), edge_labels=labels)
print(labels)

plt.show()

print(nx.dijkstra_path(G, 0, 9, weight='weight'))
