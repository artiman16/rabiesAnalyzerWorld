## Content

* [About](#info)
* [Installation](#install)
* [How to run](#run)
* [For citation](#cite)
***
## Содержание 
* [Описание](#info-ru)
* [Установка](#install-ru)
* [Запуск программы](#run-ru)
* [Для цитирования](#cite-ru)
  
## <a id="info">**About**</a>
RabiesAnalyzer is the tool created for _Lyssavirus rabies_ genomes analysis in order to determine geographical group of strains by N gene SNPs.

The algorithm of the program consists in comparing a loaded sequence with the N gene reference sequence, finding nucleotide mutations (SNP), substituting into the Sample — Mutation — Cluster table (___Clusters.csv___), which the program accepts as input during operation and which was compiled for all the "reference" strains before. The cluster to which the strain in the table belongs ("reference" strains), which has the largest number of matches for certain mutations with the test sample, is recognized as the cluster to which the test sample belongs.
***
## <a id="install">**Installation**</a>
Create new conda environment and install all necessary packages. After that activate the env. Push the python script.
It's recomended to use mamba.
```bash
mamba env create -f environment.yml
mamba activate rabiesanalyzer
python3 RabiesAnalyzer_eng.py
```
***
##  <a id="run">**How to run**</a>
### Run
After executing the script you will see the program window. To analyze the genome, select the file using the button "Open .fasta file". Launch the program using the "Analysis" button.
### Results
Below you will see the result, the group from which the strain possibly originates, and its geographical distribution.
***
## <a id="cite">**For citation:**</a>
__Герасименко А. А., Водопьянов А. С., Водопьянов С. О., Писанов, Р. В. Основы молекулярно-генетического типирования вируса бешенства в Ростовской области // Современные проблемы эпидемиологии, микробиологии и гигиены : Материалы XIV Всероссийской научно-практической конференции молодых ученых и специалистов Роспотребнадзора, Лужки, 22–24 июня 2022 года. – Москва: Федеральный научный центр гигиены им. Ф.Ф. Эрисмана, 2022. – С. 67-70_
[See the work here](https://meeting.fncg.ru/media/main/documents/1/01082022110404.pdf#page=67)
***
## <a id="info-ru">**Описание**</a>
Алгоритм работы программы состоит в сравнении загруженной последовательности с референсной N гена, нахождении нуклеотидных мутаций, подстановке в таблицу Проба — Мутации — Кластер (___Clusters.csv___), которую принимает на вход программа в ходе работы и которая была составлена для всех исследованных штаммов ранее (подробнее в статье). Кластер, к которому принадлежит штамм в таблице («референсные» 1178 штаммов), имеющий наибольшее количество совпадений по определенным мутациям с исследуемой пробой, признается кластером, к которому и относится исследуемая проба.
***
## <a id="install-ru">**Установка**</a>
После клонирования репозитория, откройте терминал в скачанной папке и создайте новое виртуальное окружение conda, установив требуемые для работы программы пакеты. Для оптимальной и быстрой установки пакетов рекомендуется использовать вместо conda mamba. 
Запустите скрипт. Команды, требуемые для работы:
```bash
mamba env create -f environment.yml
mamba activate rabiesanalyzer
python3 RabiesAnalyzer_eng.py
```
***
##  <a id="run-ru">**Запуск**</a>
### Запуск
Перед вами возникнет окно работы программы. Для анализа геномов, выберите файл по кнопке "Open .fasta file". Запустите программу по кнопке "Analysis".
### Результаты
Ниже вы сможете увидеть результат выполнения, а именно группу, откуда возможно происходит штамм, его географическое распространение.
***
## <a id="cite-ru">**Для цитирования:**</a>
_Герасименко А. А., Водопьянов А. С., Водопьянов С. О., Писанов, Р. В. Основы молекулярно-генетического типирования вируса бешенства в Ростовской области // Современные проблемы эпидемиологии, микробиологии и гигиены : Материалы XIV Всероссийской научно-практической конференции молодых ученых и специалистов Роспотребнадзора, Лужки, 22–24 июня 2022 года. – Москва: Федеральный научный центр гигиены им. Ф.Ф. Эрисмана, 2022. – С. 67-70_
[Посмотреть публикацию](https://meeting.fncg.ru/media/main/documents/1/01082022110404.pdf#page=67)