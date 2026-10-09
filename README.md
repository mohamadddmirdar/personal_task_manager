# Mini Shop
![Static Badge](![Static Badge](https://img.shields.io/badge/python-3.12-blue)
)

simple questions for customer's order
## Table of contents








  - [Table of contents](#table-of-contents)
  - [Features](#features)
  - [Project Structure](#project-structure)
    - [File Description](#file-description)
  - [Reqirments](#reqirments)
  - [Intallation](#intallation)
  - [Envoirment Setup](#envoirment-setup)
  - [Usage](#usage)
  - [Screenshot](#screenshot)
    - [programm start](#programm-start)
    - [questions](#questions)
    - [final result](#final-result)
  - [Demo](#demo)
  - [Example Output](#example-output)
  - [Roadmap](#roadmap)
  - [Contributing](#contributing)
  - [Licence](#licence)
  - [Author](#author)

## Features
- Quiz System
  - Asks the customer multiple question
  - Cheks the answers automaticlly
  - Saved orders of customers
- Result Storage
  - Saves quiz results in `sales.txt`
- Admin Mode
  - asks for the admin mode 
  - checks if the password is correct
  - keeps the private information outside the main python file
  - Loads the password from `.env`


## Project Structure

```text
|   .env.example
|   .gitignore
|   main.py
|   requirments.txt
|   README.md
|____gifs
|       demo.gif
|   pic1.png
|   pic2.png
|   pic3.png
```

### File Description
| file | description |
| --- | --- |
| `main.py` | main file used to run shop's program |
| `products.py` | the pruducts and their price |
| `.env.example` | shows the envoirment veriables neded by the projects |
| `.gitignore` | tells git which files and folders shold not be tracked. |
| `README.md` | contains the project documention |
| `pic1.png` | screenshot of the programm start |
| `ppic2.png` | screenshot of the questions |
| `pic3.png` | screenshot of the final result |
| `gifs/` | stores demo GIF files |
| `gifs\Animation.gif` | shows the project demo |

## Reqirments

Before running project, make sure you have:
- python 3
- `python-dotenv`

## Intallation

1. open a terminal in the project folder.
2. check that python is installed:
```bash
python --version
```
3. install the python packages:
```bash
pip install -r requirments.txt
```

## Envoirment Setup

1.create a `.env` file from `.env.example`:
```bash
cp .env.example .env
```
2. open the new `.env` file
3. replace the example value with your own password
```bash
ADMIN_PASSWORD = your_password
```
4. save the file
> Do not commit your `.env` file because it may contian private information.

## Usage

1. open a terminal in the project folder.
2. run the personal_task_manager 
```bash
python main.py
```
3. choose `yes` or `no` for admin mode
4. if you choose `yes`, enter the password form your `.env` file
5. enter your name 
6. answer the questions
7. see your task
8. your order is save in `sales.txt`

## Screenshot

### programm start
![programm start](pic1.png)

### questions
![questions](pic2.png)

### final result
![final_result](pic3.png)

## Demo

![demo](gifs\demo.gif)
## Example Output

```text
    what`s your name ?ali
    hi  ali
    Do you want to open admin mode? yes/no: yes
    enter admin password: q12345
    admin! hi...
    do you want add task yes or no ?  yes
    enter your task: olampiyad
    task :  olampiyad  saved
    do you want add task yes or no ?  no
```

## Roadmap

- [x] ask question about your task
- [x] add multiple tasks
- [x] save results to a file
- [x] add admin mode
- [ ] add priotority for tasks
- [ ] add a timer
## Contributing

## Licence

## Author
create by [mohamad](https://github.com/mohamad-soltani)


