# sutd-stl1

Save all files to the same folder to test the scripts. Separate modules might need to be imported by another user testing out this scripts.

**stl1_password_generator.py **
Has been set to generate 5 passwords only per character combination and length for all 6 sources and will output saved csv file stl1_all.csv:

![image](https://user-images.githubusercontent.com/39832806/136648762-2f999faa-1a6d-4809-91fd-5d24f644d805.png)


**stl1_hasher.py**
Output the MD5 hashes and populate this folder with the respective text files. An example of one of the columns in the csv, output as hash in txt file:

![image](https://user-images.githubusercontent.com/39832806/136648617-87eb2d7d-7fde-4fa3-8e1a-0577d675e90a.png)


**stl1_frequency.py**
Output the character occurrences count in descending order and populate this folder with the respective text files. An example of the top 10 most used characters in RJ source, combination 12-LDS:

![image](https://user-images.githubusercontent.com/39832806/136648715-67a6a364-605c-4f3d-9f91-7950c96f148a.png)


**stl1_tool.py**
Tool to test the password quality checker tool, scored 0 - 5 of 5 points. This tool utilizes the Levenshtein's algorithm, time taken to bruteforce and a pre-generated rainbow table. An example of an extremely weak password:

![image](https://user-images.githubusercontent.com/39832806/136648581-7319f88c-c0c2-4afa-b6b1-9de17a3ada4e.png)

