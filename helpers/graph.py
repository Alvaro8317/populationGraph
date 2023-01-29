import matplotlib.pyplot as plt 


def generate_bar_chart(labels, values):
    fig, ax = plt.subplots()  # Matplot trae dos variables
    ax.bar(labels, values)
    plt.show()


def generate_pie_chart(labels, values):
    fig, ax = plt.subplots()  # Matplot trae dos variables
    ax.pie(values, labels=labels)
    ax.axis('equal')
    plt.show()



def create_a_graph(data, form):
    labels_data = [key for key, value in data.items()]
    labels_data = labels_data[1:]
    labels_data.reverse()
    values_data = [value for key, value in data.items()]
    values_data = values_data[1:]
    values_data.reverse()
    print(labels_data, values_data)
    if form == "bar":
        generate_bar_chart(labels_data, values_data)
    elif form == "pie":
        generate_pie_chart(labels_data, values_data)
    else:
        print("Invalid form, I shouldn't appear")