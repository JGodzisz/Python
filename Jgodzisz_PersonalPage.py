#Jeffrey Godzisz
#Personal Web page generator
#CSC 121-01SY

def main():
    #open a writable file
    file = open('webPage.html', 'w')
    #request input
    name = input("Enter Your Name:")
    major = input("Enter Your Degree/Major:")
    career = input("Enter your future career and a brief description of the career:")
    #call the function to write the html
    write_html(file, name, major, career)
    #close the file
    file.close()

#define the function to write html
def write_html(file, name, major, career):
    #write the opening tag and call the other functions then close the html
    file.write('<html> \n')
    write_head(file)
    write_body(file, name, major, career)
    file.write('</html>')

#define the function to write the head of the webpage
def write_head(file):
    #write the opening tags, title, and closing tags for head and title
    file.write('<head> \n')
    file.write('<title> \n')
    file.write("My Personal Web Page \n")
    file.write('</title> \n')
    file.write('</head> \n')

#define the function to write the body of the webpage
def write_body(file, name, major, career):
    #write the opening tag, center format tag, user input and close tags
    file.write('<body> \n')
    file.write('\t <center> \n')
    heading = '\t\t <h1>' + name + '</h1> \n'
    file.write(heading)
    file.write('\t\t <hr /> \n')
    heading2 = '\t\t <h2>' + major + '</h2> \n'
    file.write(heading2)
    file.write('\t <hr /> \n')
    body = '\t' + career
    file.write(body)
    file.write('\t </center> \n')
    file.write('\t <hr /> \n')
    file.write('</body>')
    #Variables were made durring debugging decided to keep them
    
if __name__ == '__main__':
    main()
