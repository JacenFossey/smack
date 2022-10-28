import click
import os

@click.command()
@click.argument('project_name', required=True)

def main(project_name: str):

  project_title = project_name+"_project"
  # creates the main folder
  def create_main_folder():
    try:
      os.mkdir(project_title)
      print(f"Directory /{project_title} created")
    except FileExistsError:
      print(f"Directory /{project_title} already exists")

  

  # creates the src folder
  def create_src_folder():

    # current_dir/project_name
    cwdir = os.getcwd()+"/"+project_title

    try:
      os.mkdir(cwdir+"/src")
      print("Directory /src created")
    except FileExistsError:
      print("The folder /src already exists")
      
    # creates the subsrc folder
    def create_subsrc_folder():
      cwdir = os.getcwd()+"/"+project_title+"/src"
      try:
        os.mkdir(cwdir+"/"+project_name)
        print(f"Directory /{project_name} created")
      except FileExistsError:
        print(f"Directory /{project_name} already exists")

      def create_init():
        cwdir = os.getcwd()+"/"+project_title+"/src/"+project_name
        try:
          file = open(cwdir+"/__init__.py", "x")
          print("File __init__.py created")
        except FileExistsError:
          print("File __init__.py already exists")

      def create_main_file():
        cwdir = os.getcwd()+"/"+project_title+"/src/"+project_name
        try:
          file = open(cwdir+"/"+project_name+".py", "x")
          print(f"File {project_name}.py created")
        except FileExistsError:
          print(f"File {project_name}.py already exists")
        
      create_init()
      create_main_file()

    create_subsrc_folder()

  def create_tests_folder():
    cwdir = os.getcwd()+"/"+project_title

    try:
      os.mkdir(cwdir+"/tests")
      print("Directory /tests created")
    except FileExistsError:
      print("Directory /tests already exists")

  def create_license():
    cwdir = os.getcwd()+"/"+project_title
    try:
      file = open(cwdir+"/LICENSE.txt", "x")
      print("File LICENSE created")
    except FileExistsError:
      print("File LICENSE already exists")

  def create_pyprojecttoml():
    cwdir = os.getcwd()+"/"+project_title
    try:
      file = open(cwdir+"/pyproject.toml", "x")
      print("File pyproject.toml created")
    except:
      print("File pyproject.toml already exists")

  def create_readme():
    cwdir = os.getcwd()+"/"+project_title
    try:
      file = open(cwdir+"/README.md", "x")
      print("File README.md created")
    except:
      print("File README.md already exists")
    
  create_main_folder()
  create_src_folder()
  create_tests_folder()
  create_license()
  create_pyprojecttoml()
  create_readme()


  
if __name__ == '__main__':
    main()