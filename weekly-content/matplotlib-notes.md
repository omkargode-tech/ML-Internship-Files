
---

MATPLOTLIB PLOTS CUSTOMIZATION NOTES (PIE, HISTOGRAM, BOXPLOT, BAR, SCATTER)

---

## PIE CHART CUSTOMIZATION (plt.pie)

Basic:
plt.pie(values, labels=labels)

Show percentage:
autopct='%1.1f%%'

Show values instead of percentage:
Use custom function in autopct:

def func(pct):
total = sum(values)
val = int(round(pct * total / 100))
return str(val)

plt.pie(values, labels=labels, autopct=func)

Explode (spacing between slices):
explode = [0.1, 0, 0, 0]

Colors:
colors = ['red', 'blue', 'green']

Other options:
startangle=90
shadow=True
wedgeprops={'edgecolor':'black'}
textprops={'fontsize':12}

Donut chart:
plt.pie(values, wedgeprops={'width':0.4})

---

## HISTOGRAM CUSTOMIZATION (plt.hist)

Basic:
plt.hist(data, bins=5)

Common options:
bins = number or list of edges
color = 'skyblue'
edgecolor = 'black'
alpha = 0.5
rwidth = 0.8

Histogram types:
histtype='bar'
histtype='step'
histtype='stepfilled'

Density instead of frequency:
density=True

Grid:
plt.grid(axis='y')

Horizontal histogram:
orientation='horizontal'

FREQUENCY POLYGON ON HISTOGRAM:

counts, bins, _ = plt.hist(data, bins=5)

midpoints = (bins[:-1] + bins[1:]) / 2

plt.plot(midpoints, counts)

---

## BOX PLOT CUSTOMIZATION (plt.boxplot)

Basic:
plt.boxplot(data)

Fill color:
patch_artist=True
boxprops=dict(facecolor='lightblue')

Median line:
medianprops=dict(color='red', linewidth=2)

Whiskers:
whiskerprops=dict(color='black', linestyle='--')

Outliers:
flierprops=dict(marker='o', color='red')

Show mean:
showmeans=True
meanprops=dict(marker='D', color='green')

Horizontal boxplot:
vert=False

Notch box:
notch=True

---

## BAR CHART CUSTOMIZATION (plt.bar)

Basic:
plt.bar(categories, values)

Color:
color='skyblue'

Multiple colors:
color=['red','green','blue']

Edge:
edgecolor='black'
linewidth=1

Bar width:
width=0.5

Horizontal bar:
plt.barh(categories, values)

Add values on bars:
bars = plt.bar(...)
plt.bar_label(bars)

Hatching pattern:
hatch='//'

Grouped bars:
use numpy + shift x positions

Stacked bars:
plt.bar(x, y1)
plt.bar(x, y2, bottom=y1)

---

## SCATTER PLOT CUSTOMIZATION (plt.scatter)

Basic:
plt.scatter(x, y)

Color:
color='red'

Different colors:
c=values
cmap='viridis'

Marker styles:
'o' circle
's' square
'^' triangle
'*' star

Size:
s=[10,50,100]

Transparency:
alpha=0.5

Edge:
edgecolor='black'

Colorbar:
plt.colorbar()

Annotations:
plt.text(x, y, "label")

Grid:
plt.grid(True)

---

## IMPORTANT GENERAL SETTINGS

Title:
plt.title("Title")

Labels:
plt.xlabel("X")
plt.ylabel("Y")

Figure size:
plt.figure(figsize=(8,5))

Grid:
plt.grid(True, linestyle='--', alpha=0.5)

Show:
plt.show()

