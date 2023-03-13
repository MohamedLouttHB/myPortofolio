import streamlit as st
from PIL import Image
import subprocess

with open("style.css") as f:
    st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)

#####################

# Header
st.write('''
# Mohamed Loutt Horma Babana
##### *Resume* 
''')

image = Image.open('profil.png')
st.image(image, width=200)

# Create a button to open the PDF file
if st.button('📄View Resume'):
    subprocess.call(["open", "CV.pdf"])

st.markdown('## Summary', unsafe_allow_html=True)
st.info('''
- I am a master student in data science and engineering, passionate about data science, artificial intelligence and machine learning.
- knowledge of business management and an entrepreneurial spirit.
- Ability to communicate, listen - write - comprehend and teamwork''')

#####################
# Navigation

st.markdown(
    '<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">',
    unsafe_allow_html=True)

st.markdown("""
<nav class="navbar fixed-top navbar-expand-lg navbar-dark" style="background-color: #16A2CB;">
  <a class="navbar-brand" href="/" target="">Portofolio</a>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>
  <div class="collapse navbar-collapse" id="navbarNav">
    <ul class="navbar-nav">
      <li class="nav-item">
        <a class="nav-link" href="#education">Education</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#certificates">Certificates</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#projects">Projects</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#skills">Skills</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#contact">Contact</a>
      </li>
    </ul>
  </div>
</nav>
""", unsafe_allow_html=True)


#####################
# Custom function for printing text
def txt(a, b):
    col1, col2 = st.columns([4, 1])
    with col1:
        st.markdown(a)
    with col2:
        st.markdown(b)


def txt2(a, b):
    col1, col2 = st.columns([1, 4])
    with col1:
        st.markdown(f'`{a}`')
    with col2:
        st.markdown(b)


def txt3(a, b):
    col1, col2 = st.columns([1, 2])
    with col1:
        st.markdown(a)
    with col2:
        st.markdown(b)


def txt4(a, b, c):
    col1, col2, col3 = st.columns([1.5, 2, 2])
    with col1:
        st.markdown(f'`{a}`')
    with col2:
        st.markdown(b)
    with col3:
        st.markdown(c)


#####################
st.markdown('''
## Education
''')

txt('- **Baccalauréate** (Mathematic), *El Khiyar School*, Mauritania',
    '2017-2018')
txt('- **License MIAGE** (IT Methods Applied to Business Managment), *Faculty of Science and Technology , University of Nouakchott*, Mauritania',
    '2021-2022')
txt('- **Master\'s in Data Science and Engineering** , *Universié Mohamed V *,Faculty of Sciences of Rabat, Morrocco',
    '2021-2022')

#####################

st.markdown('''
## Certificates
''')
txt2('Python for Data Science, AI & Development ', 'https://www.coursera.org/account/accomplishments/certificate/KNM83354PQAD')
txt2('Databases and SQL for Data Science with Python', 'https://www.coursera.org/account/accomplishments/certificate/KNM83354PQAD')


#####################
st.markdown('''
## Projects
''')

txt('**Managment of Faculty Classrooms**, Second years of my IT license,',
    '2019-2020')
st.markdown('''
**Tools**
- HTML, CSS, JS, PHP
- MySQL
''')

txt('**Sales Managment Desktop Application**, End of Studies Project,',
    '2020-2021')
st.markdown('''
**Tools**
- C# ( Windows Forms )
- Microsoft SQL Server
''')

#####################
st.markdown('''
## Skills
''')
txt3('👨‍💻 Programming', '`Python`, `Java`, `R`')
txt3('📚Data processing/wrangling', '`pandas`, `numpy`, `SQL`')
txt3('📊 Data visualization', '`matplotlib`, `seaborn`, `plotly`, `ggplot2`')
txt3('🤖 Machine Learning', '`scikit-learn`')
txt3('🧠 Deep Learning', '`TensorFlow`')
txt3('🌐 Web development', '`Django`, `Streamlit`, `Vue.js`, `HTML`, `CSS`')
txt3('🗄️️ Databases', '`MySQL`, `SQL Server`, `Oracle`')
txt3('🚀 Model deployment', '`streamlit`, `R Shiny`, `Heroku`, `AWS`')

#####################
st.markdown('''
## Contact
''')
txt2('LinkedIn', 'https://www.linkedin.com/in/mohamed-loutt-horma-babana-5619011aa')
txt2('Email', 'm.loutt99@gmail.com')
