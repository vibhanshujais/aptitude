from django.shortcuts import render
from aptitudes.models import aptitude
from aptitudes.models import algorithm
from aptitudes.models import vocabulary

def home(request):
    return render(request,"home.html")

def quants(request):
    a = aptitude.objects.filter(category='QUANTS')
    data = {'key':a}
    x=[]
    for i in data["key"]:
        x.append(str(i))
    topic_set = sorted(set(x))
    return render(request,"quants.html",{'key':topic_set})

def reasoning(request):
    a = aptitude.objects.filter(category='REASONING')
    data = {'key':a}
    x=[]
    for i in data["key"]:
        x.append(str(i))
    topic_set = sorted(set(x))
    return render(request, "reasoning.html",{'key':topic_set})

def english(request):
    a = aptitude.objects.filter(category='ENGLISH')
    data = {'key':a}
    x=[]
    for i in data["key"]:
        x.append(str(i))
    topic_set = sorted(set(x))
    return render(request, "english.html",{'key':topic_set})

def questions(request,topic_name):
    a = aptitude.objects.filter(topic=topic_name).values()
    return render(request, "question.html",{'key':a})

def blogs(request):
    return render(request,"blogs.html")

def algo(request):
    a = algorithm.objects.filter(category='algo')
    data = {'key':a}
    x =[]
    for i in data["key"]:
        x.append(str(i))
    return render(request, "algorithm.html",{'key':x})

def algorithms(request,algo_name):
    a = algorithm.objects.filter(category='algo')
    data = {'key':a}
    if algo_name=="Linear search":
        return render(request,"linear.html",data)
    if algo_name=="Binary Search":
        return render(request,"binary.html",data)
    if algo_name=="Bubble sort":
        return render(request,"bubble.html",data)
    if algo_name=="Selection sort":
        return render(request,"selection.html",data)
    if algo_name=="Insertion sort":
        return render(request,"insertion.html",data)
    if algo_name=="Merge sort":
        return render(request,"merge.html",data)
    if algo_name=="Quick sort":
        return render(request,"quick.html",data)
    if algo_name=="Counting sort":
        return render(request,"count.html",data)
    if algo_name=="Radix sort":
        return render(request,"radix.html",data)
    if algo_name=="BFS":
        return render(request, "bfs.html",data)
    if algo_name=="DFS":
        return render(request, "dfs.html",data)
    if algo_name=="Prim's Algorithm":
        return render(request, "prim.html",data)
    if algo_name=="Kruksal's Algorithm":
        return render(request, "kruksal.html",data)
    if algo_name=="Heap Sort":
        return render(request, "heap.html",data)
    if algo_name=="Floyd-Warshall Algorithm":
        return render(request, "floyd.html",data)
    if algo_name=="Djikstra's Algorithm":
        return render(request, "djikstra.html",data)
    if algo_name=="Bellman-Ford Algorithm":
        return render(request, "bellman.html",data)
    if algo_name=="Bucket Sort":
        return render(request, "bucket.html",data)
def vocabs(request):
    a = vocabulary.objects.filter(category='vocabulary')
    data={'key':a}
    x=[]
    for i in data["key"]:
        x.append(str(i))
    topic_set = sorted(set(x))
    return render(request, "vocabs.html", {'key':topic_set})

def vocab(request,topic):
    a = vocabulary.objects.filter(topic=topic)
    data= {'key':a}
    x=[]
    for i in data["key"]:
        if i not in x:
            x.append(str(i))
            break
    print(x)
    return render(request, "vocab.html",{'key':a, 'data':x})