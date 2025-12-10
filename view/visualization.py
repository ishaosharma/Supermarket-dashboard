#view/: Contains code for data visualization.
import matplotlib.pyplot as plt
import numpy as np

def plot_bar(labels, values, title, xlabel, ylabel):
    plt.figure(figsize=(10,6))
    plt.bar(labels, values, color='teal')
    plt.title(title, fontsize=16, weight='bold')
    plt.xlabel(xlabel, fontsize=12)
    plt.ylabel(ylabel, fontsize=12)
    plt.xticks(rotation=45, fontsize=10)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    return plt 

def plot_pie(labels, values, title):
    plt.figure(figsize=(8,8)) 
    plt.pie(values, labels=labels, autopct='%1.1f%%', startangle=140, colors=plt.cm.Pastel1.colors)
    plt.title(title, fontsize=16, weight='bold')
    plt.tight_layout() 
    return plt 

def plot_line(labels, values, title, xlabel, ylabel):
    plt.figure(figsize=(10,6))
    plt.plot(labels, values, marker='o', linestyle='-', color='darkblue', linewidth=2)
    plt.fill_between(labels, values, color='lightblue', alpha=0.4)
    plt.title(title, fontsize=16, weight='bold')
    plt.xlabel(xlabel, fontsize=12)
    plt.ylabel(ylabel, fontsize=12)
    plt.xticks(rotation=45)
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.tight_layout()
    return plt

def plot_scatter(x, y, title, xlabel, ylabel):
    plt.figure(figsize=(10,6))
    plt.scatter(x, y, color='mediumseagreen', edgecolor='black', alpha=0.7, s=80)
    plt.title(title, fontsize=16, weight='bold')
    plt.xlabel(xlabel, fontsize=12)
    plt.ylabel(ylabel, fontsize=12)
    plt.grid(True, linestyle='--', alpha=0.5)
    plt.tight_layout()
    return plt

