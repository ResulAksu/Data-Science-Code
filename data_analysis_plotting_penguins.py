import numpy as np
from scipy import stats as st
from matplotlib import pyplot as plt


url = "https://raw.githubusercontent.com/mcnakhaee/palmerpenguins/master/palmerpenguins/data/penguins.csv"

#Name des verwendeten Datensatz: palmerpenguins

#Quelle: url = "https://github.com/mcnakhaee/palmerpenguins/blob/master/palmerpenguins/data/penguins.csv"
#Lizens: Data are available by CC-0 license in accordance with the Palmer Station LTER Data Policy and the LTER Data Access Policy for Type I data.
#Autor: Gorman KB, Williams TD, Fraser WR (2014) Ecological Sexual Dimorphism and Environmental Variability within a Community of Antarctic Penguins (Genus Pygoscelis).

#Zeilen 344 + 1 Header
#Aufgeteilt in 8 Attribute, spezie, insel, Schnabellänge, Schnabeltiefe, Flügellänge, Gewicht, Geschlecht, Jahr
dtype = [('species', '<U10'), ('island', '<U10'), ('bill_length_mm', float), ('bill_depth_mm', float), ('flipper_length_mm', int), ('body_mass_g', int), ('sex', '<U10'), ('year', int)]
data = np.genfromtxt(url, delimiter=',', names= True, dtype=dtype)

print(type(data), data.shape, data.shape[0], len(data[0]))


#--------------------------------------------------
#Frage: Schwerstes Gewicht der von allen Spezien
speci = np.unique(data["species"])
max_body_mass_list = []

for specie in speci:
    body_mass = data[data["species"] == specie]["body_mass_g"]
    max_body_mass = np.max(body_mass)
    max_body_mass_list.append(max_body_mass)

print(speci, max_body_mass_list)

# Plot
plt.bar(speci, max_body_mass_list)
plt.xlabel('Species')
plt.ylabel('Max Body Mass (g)')
plt.title('Maximum Body Mass for Each Species')
plt.xticks(rotation=90)
plt.show()
#--------------------------------------------------
#Zusammenfassen aller vorhandenen Spezienanzahl
unique_species = np.unique(data["species"])
species_count = np.sum(np.equal(data["species"][:,None], unique_species), axis=0)

for specie, count in zip(unique_species, species_count):
    print(specie, ":", count)
print()

#Plot
x = np.arange(len(unique_species))

plt.bar(x, species_count)
plt.xlabel('Species')
plt.ylabel('Count')
plt.title('Count of Unique Species')
plt.xticks(x, unique_species, rotation='vertical')
plt.tight_layout()
plt.show()
#--------------------------------------------------
#Durschnittsgewicht pro Spezie
mean_weights = {}

for sp in unique_species:
    specie_data = data[data["species"] == sp]

    weights = specie_data["body_mass_g"].astype(float)

    mean_weight = np.mean(weights)

    mean_weights[sp] = mean_weight

print( mean_weights)
print()

speciese = list(mean_weights.keys())
mean_weights_values = list(mean_weights.values())

# Plotting
x = np.arange(len(speciese))

plt.bar(x, mean_weights_values)
plt.xlabel('Species')
plt.ylabel('Mean Weight')
plt.title('Mean Weight by Species')
plt.xticks(x, speciese, rotation='vertical')
plt.tight_layout()
plt.show()
#--------------------------------------------------
#Geschlechterverhältnis pro Insel

sex = data["sex"]
island = data["island"]

unique_islands = np.unique(island)

male_ratios = []
female_ratios = []

for isl in unique_islands:
    island_mask = (island == isl)
    island_sex = sex[island_mask]
    male_count = np.count_nonzero(island_sex == "male")
    female_count = np.count_nonzero(island_sex == "female")
    total_count = male_count + female_count
    male_ratio = male_count / total_count
    female_ratio = female_count / total_count
    print("Island:", isl)
    print("Male Ratio:", male_ratio)
    print("Female Ratio:", female_ratio)
    print()
    male_ratios.append(male_ratio)
    female_ratios.append(female_ratio)


#Plot
x = np.arange(len(unique_islands))
width = 0.35

fig, ax = plt.subplots()
bar1 = ax.bar(x - width/2, male_ratios, width, label='Male Ratio')
bar2 = ax.bar(x + width/2, female_ratios, width, label='Female Ratio')

ax.set_xlabel('Island')
ax.set_ylabel('Ratio')
ax.set_title('Male-Female Ratio by Island')
ax.set_xticks(x)
ax.set_xticklabels(unique_islands)
ax.legend()

plt.show()

#--------------------------------------------------
#Auf einer insel meisten populiert
most_common_species = {}
species = data["species"]

for isl in unique_islands:
    island_mask = (island == isl)
    island_species = species[island_mask]
    
    unique_species, counts = np.unique(island_species, return_counts=True)
    
    most_common_species_index = np.argmax(counts)
    most_common_species_name = unique_species[most_common_species_index]
    
    most_common_species[isl] = most_common_species_name

    if len(np.unique(island_species)) > 1:
        print("Die Insel", isl, "hat mehr als eine Art.")
    else:
        print("Die Insel", isl, "hat nur eine Art.")
print()
for isl, common_species in most_common_species.items():
    print("Insel:", isl, "- Am meisten verbreitete Spezies:", common_species)

# Plotting
x = np.arange(len(unique_islands))
common_species_values = list(most_common_species.values())

plt.bar(x, common_species_values)
plt.xlabel('Island')
plt.ylabel('Most Common Species')
plt.title('Most Common Species per Island')
plt.xticks(x, unique_islands, rotation='vertical')
plt.tight_layout()
plt.show()
#--------------------------------------------------