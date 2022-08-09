# -*- coding: utf-8 -*-
import os # Pour la manipulation des dossiers
import shutil # Pour la manipulation des fichiers
import traceback # Pour la gestion des erreurs
import Settings
import Interact

class Project:
    def __init__(self,ProjectName,WorkingDir,LaTeXClass):
        self.ProjectName = ProjectName
        self.WorkingDir = WorkingDir
        self.LaTeXClass = LaTeXClass
    
    def CheckClass(self):
        if self.LaTeXClass not in Settings.ClassList:
            raise("Ceci n'est pas une classe supportée")
    
    def CreateProject(self,images=True,pptx=False):
        Interact.MakeFolder(self.WorkingDir,self.ProjectName)
        ListFile = os.listdir(Settings.PathToSource)
        Project.CheckClass(self)
        # utiliser la fonction pour checker si packages.sty ou bristol sont utilisés,
    
    def RemoveProject(self):
        pass
    

