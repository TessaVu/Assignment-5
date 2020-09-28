# Tessa Vu

# 5-1: Word Statistics
# Please analyze this paragraph by counting the number of sentences it contains.

paragraph = "Geography is the study of natural Earth systems, human societies and the interaction between them. Geography bridges the physical and social sciences. Geographers work with powerful technologies such as geographic information systems (GIS), digital Earth imagery (remote sensing) and spatial modeling. And geographers are not afraid to get their boots muddy. Geography has a long-standing field tradition, often involving travel to spectacular locations. Geographers use a collaborative and integrated approach to help understand complex 21st century challenges such as climate change, globalization, sustainability, urbanization, and living with hazards. Rewarding careers exist in the private and public sectors, and education."
count = 0
for period in paragraph:
	if period == ".":
		count += 1
print("There are", count, "sentences in this paragraph.")

# 5-2: Student Score Ranking
# Format is "student_name, math_score, writing_score".
# Process the string and print their scores in this format: "Name: Wakeeta; Math: 90; Writing: 93;"
# Calculate and print out who received the highest and lowest total score and their scores.

scores = "Wakeeta,90,93;Jia-Wen,87.5,93;Roberto,89,96.5;Akiko,93,87;Maurice,89,86"
