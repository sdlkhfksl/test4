import requests

url = 'https://ghproxy.com/https://raw.githubusercontent.com/youshandefeiyang/IPTV/main/main/aishang.m3u'

response = requests.get(url)
text = response.text

# Add "央视（爱尚）,#genre#" and "卫视（爱尚）,#genre#" at the beginning of the file
text = text.replace('#EXTM3U', '央视（爱尚）,#genre#\n#EXTM3U', 1)
text = text.replace('*卫视', '卫视（爱尚）,#genre#\n*卫视', 1)

# Split the text into lines
lines = text.splitlines()

# Process each group of data and extract the first line containing "CCTV" or "卫视"
processed_lines = []
for i in range(0, len(lines), 2):
    if 'CCTV' in lines[i] or '卫视' in lines[i]:
        name = lines[i].split(',')[-1].strip()
        url = lines[i+1]
        processed_lines.append(f'{name},{url}')

# Add "央视（爱尚）,#genre#" at the beginning of the file
processed_lines.insert(0, '央视（爱尚）,#genre#')

# Add "卫视（爱尚）,#genre#" above the first occurrence of "卫视"
for i, line in enumerate(processed_lines):
    if '卫视' in line:
        processed_lines.insert(i, '卫视（爱尚）,#genre#')
        break

# Save the processed data to a file
with open('4.txt', 'w', encoding='utf-8') as f:
    f.write('\n'.join(processed_lines))

url = 'https://ghproxy.com/https://raw.githubusercontent.com/youshandefeiyang/IPTV/main/main/bestv.m3u'

response = requests.get(url)
text = response.text

# Add "央视（爱尚）,#genre#" and "卫视（爱尚）,#genre#" at the beginning of the file
text = text.replace('#EXTM3U', '央视（爱尚）,#genre#\n#EXTM3U', 1)
text = text.replace('*卫视', '卫视（爱尚）,#genre#\n*卫视', 1)

# Split the text into lines
lines = text.splitlines()

# Process each group of data and extract the first line containing "CCTV" or "卫视"
processed_lines = []
for i in range(0, len(lines), 2):
    if 'CCTV' in lines[i] or '卫视' in lines[i]:
        name = lines[i].split(',')[-1].strip()
        url = lines[i+1]
        processed_lines.append(f'{name},{url}')

# Add "央视（爱尚）,#genre#" at the beginning of the file
processed_lines.insert(0, '央视（BESTV）,#genre#')

# Add "卫视（BESTV）,#genre#" above the first occurrence of "卫视"
for i, line in enumerate(processed_lines):
    if '卫视' in line:
        processed_lines.insert(i, '卫视（BESTV）,#genre#')
        break

# Save the processed data to a file
with open('2.txt', 'w', encoding='utf-8') as f:
    f.write('\n'.join(processed_lines))

url = 'https://ghproxy.com/https://raw.githubusercontent.com/fanmingming/live/main/tv/m3u/global.m3u'

response = requests.get(url)
text = response.text

# Add "央视（爱尚）,#genre#" and "卫视（爱尚）,#genre#" at the beginning of the file
text = text.replace('#EXTM3U', '央视（爱尚）,#genre#\n#EXTM3U', 1)
text = text.replace('*卫视', '卫视（爱尚）,#genre#\n*卫视', 1)

# Split the text into lines
lines = text.splitlines()

# Process each group of data and extract the first line containing "CCTV" or "卫视"
processed_lines = []
for i in range(0, len(lines), 2):
    if 'CCTV' in lines[i] or '卫视' in lines[i]:
        name = lines[i].split(',')[-1].strip()
        url = lines[i+1]
        processed_lines.append(f'{name},{url}')

# Add "央视（爱尚）,#genre#" at the beginning of the file
processed_lines.insert(0, '央视（FMM）,#genre#')

# Add "卫视（BESTV）,#genre#" above the first occurrence of "卫视"
for i, line in enumerate(processed_lines):
    if '卫视' in line:
        processed_lines.insert(i, '卫视（FMM）,#genre#')
        break

# Save the processed data to a file
with open('3.txt', 'w', encoding='utf-8') as f:
    f.write('\n'.join(processed_lines))

# Read the contents of each file
with open('4.txt', 'r', encoding='utf-8') as f:
    file1_content = f.read()

with open('2.txt', 'r', encoding='utf-8') as f:
    file2_content = f.read()

with open('3.txt', 'r', encoding='utf-8') as f:
    file3_content = f.read()

# Combine the contents into a single string
combined_content = file1_content + '\n' + file2_content + '\n' + file3_content

# Write the combined content to a file
with open('1.txt', 'w', encoding='utf-8') as f:
    f.write(combined_content)
