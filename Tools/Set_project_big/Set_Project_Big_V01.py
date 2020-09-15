from tkinter import *
from tkinter.filedialog import askdirectory
import os
import shutil

def dirs(dir) :
	prePath = entr2.get() + '/' + entr1.get() + '/' # Chemin determiné par utilisateur + nom du dossier
	os.makedirs (prePath + dir) 

def dirCre():
	"Creer le pipeline"
	dirs ('01_Gestion_de_production/01_Brief')
	dirs ('01_Gestion_de_production/02_Planning')
	dirs ('01_Gestion_de_production/03_Compte_Rendu')
	dirs ('01_Gestion_de_production/04_Annexes')
	dirs ('02_Pre_Production/01_Sources/01_3D')
	dirs ('02_Pre_Production/01_Sources/02_Videos')
	dirs ('02_Pre_Production/01_Sources/03_Images')
	dirs ('02_Pre_Production/01_Sources/04_Audio/01_Sound_Design')
	dirs ('02_Pre_Production/01_Sources/04_Audio/02_Music')
	dirs ('02_Pre_Production/01_Sources/04_Audio/03_Voice')
	dirs ('02_Pre_Production/01_Sources/04_Audio/04_Master')
	dirs ('02_Pre_Production/02_Storyboard')
	dirs ('02_Pre_Production/03_Direction_Artistique/01_Benchmark')
	dirs ('02_Pre_Production/03_Direction_Artistique/02_Creation')
	dirs ('02_Pre_Production/04_Casting')
	dirs ('03_Production/01_Creation/01_Modeling/01_Characters')
	dirs ('03_Production/01_Creation/01_Modeling/02_Environment_and_Props')
	dirs ('03_Production/01_Creation/01_Modeling/03_Proxies')
	dirs ('03_Production/01_Creation/02_Texturing/01_UVs')
	dirs ('03_Production/01_Creation/02_Texturing/02_Maps')
	dirs ('03_Production/01_Creation/02_Texturing/03_MatLib')
	dirs ('03_Production/01_Creation/03_Rigging')
	dirs ('03_Production/01_Creation/04_Lighting')
	dirs ('03_Production/02_Animation/01_Layout')
	dirs ('03_Production/02_Animation/02_Animation/01_Bip')
	dirs ('03_Production/02_Animation/03_FX/01_RealFlow/01_Cache')
	dirs ('03_Production/02_Animation/03_FX/01_RealFlow/02_Presets')
	dirs ('03_Production/02_Animation/03_FX/02_FumeFx/01_Cache')
	dirs ('03_Production/02_Animation/03_FX/02_FumeFx/02_Presets')
	dirs ('03_Production/02_Animation/03_FX/03_RayFire/01_Cache')
	dirs ('03_Production/02_Animation/03_FX/03_RayFire/02_Presets')
	dirs ('03_Production/03_Final_Images/01_Final_Scenes')
	dirs ('03_Production/03_Final_Images/02_GI/01_Light_Cache')
	dirs ('03_Production/03_Final_Images/02_GI/02_Irradiance_Map')
	dirs ('03_Production/03_Final_Images/03_Render_Presets')
	dirs ('03_Production/03_Final_Images/04_Render_Output')
	dirs ('03_Production/04_Autoback')
	dirs ('03_Production/05_Export/01_Cameras')
	dirs ('03_Production/05_Export/02_Lights')
	dirs ('03_Production/05_Export/03_Characters')
	dirs ('03_Production/05_Export/04_Environment_and_Props')
	dirs ('03_Production/05_Export/05_Max2AE')
	dirs ('03_Production/06_Scripts')
	dirs ('03_Production/07_Plugins')
	dirs ('04_Post_Production/01_Montage/01_Footages')
	dirs ('04_Post_Production/02_Tracking')
	dirs ('04_Post_Production/03_Compositing/01_Export')
	dirs ('04_Post_Production/03_Compositing/02_Script/01_AE')
	dirs ('04_Post_Production/03_Compositing/02_Script/02_Nuke')
	dirs ('04_Post_Production/04_Audio')
	dirs ('05_Engine')
	dirs ('05_Engine/01_Projects')
	dirs ('05_Engine/02_Backups')
	dirs ('05_Engine/02_Backups/01_DailyBackups')
	dirs ('05_Engine/02_Backups/02_Backups')
	dirs ('06_WIP/01_3dsMax_Preview')
	dirs ('06_WIP/02_Animatique')
	dirs ('07_Delivery')
	
	#shutil.copy2('/Users/yanndrevon/Desktop/1080p_25fps.aep', pth1) # Copie les fichiers nécéssaires aux bons emplacements
	
	
def GetPth() :
	"Récuperer le chemin"
	filename = askdirectory()
	content.set(filename)


# Définition fenetre
fen1 = Tk()
fen1.title("Set Project")
fen1.config(background='#404040')
# fen1.geometry("780x300")

# Textes devant champs textuel 
txt1 = Label(fen1, text = 'Nom du projet :', font=("Helvetica", 10), bg='#404040', fg=('#FFFFFF'))
txt2 = Label(fen1, text = 'Chemin:', font=("Helvetica", 10), bg='#404040', fg=('#FFFFFF'))

# Champs Textuels
content = StringVar()
entr1 = Entry(fen1)
entr2 = Entry(fen1, textvariable = content)

# Mise en page
txt1.grid(row = 0)
txt2.grid(row = 1)

entr1.grid(row = 0, column = 1)
entr2.grid(row = 1, column = 1)

b2 = Button(fen1, text = "Browse", font=("Helvetica", 10), bg='#404040', fg=('#FFFFFF'), command = GetPth)
b2.grid(row = 1, column = 2)
b2 = Button(fen1, text = "Créer", font=("Helvetica", 10), bg='#404040', fg=('#FFFFFF'), command = dirCre)
b2.grid(row = 3, column = 1)

fen1.mainloop()

#if not os.path.exists(newpath): os.makedirs(newpath)