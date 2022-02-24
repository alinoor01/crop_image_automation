import cv2
import os
import matplotlib.pyplot as plt

#get current directory 
this_directory = os.getcwd()
new_folder_name = "cropped_photos"

def get_directory_names_and_directory(dir):
    directory_dictionary = {}
    # os.listdir(dir) to get all files and folders, os.path.isdir(name)to get only directories
    try :
        for folder_name in os.listdir(dir): 
            if os.path.isdir(folder_name) :
                directory_dictionary[folder_name] = os.path.join(dir, folder_name)
        return directory_dictionary
    except FileExistsError as e :
        print(e)
        pass


def crete_folder_and_subfolders(this_dir, this_dic):
    new_folder_path = os.path.join(this_dir, new_folder_name)
    # use key to get the names of original subfolders
    try : 
        os.mkdir(new_folder_path)
        for key,val in this_dic.items():
            if os.path.isdir(key):
                sub_folder_path = os.path.join(new_folder_path, key)
                os.mkdir(sub_folder_path+'_'+new_folder_name)
        return new_folder_path
    except FileExistsError as e :
        print("File exists", e)
        #pass


def crop_photos(main_photo_directory, cropped_photo_store_dir):
    # get the folders with images inside
    for key_folder_names, value_folder_path in main_photo_directory.items() :
        if value_folder_path == os.path.join(this_directory, new_folder_name):
            print("cropped folder passed")
            pass
        else :
            #take each photo and crop 
            for image_list in os.listdir(value_folder_path) :
                mypath = os.path.join(value_folder_path, image_list)
                myimage = cv2.imread(mypath)
                crop_img = myimage[10:10+940, 480:480+300]

                saveimgpath = os.path.join(this_directory , new_folder_name, key_folder_names+"_"+new_folder_name, image_list)
                print(saveimgpath)
                cv2.imwrite(saveimgpath , crop_img )

                #plt.imshow(crop_img)
                #plt.show()

def confirm_crop_position():
    mypath = '/home/nvidia/Desktop/trainning_data/Hard_Ko/495R_900_20210618_13üF01üF04.png'
    myimage = cv2.imread(mypath)
    myimage = cv2.cvtColor(myimage, cv2.COLOR_BGR2RGB)
    myimage = cv2.rectangle(myimage, (480,10), (780,950), (255,0,0,), 2)

    # plt.imshow(myimage)
    # plt.show()


def main():
    #get path and list of existing folders in the current directory and make a dictionary {folder_name : path_of_that_folder}
    folder_directory_dic = get_directory_names_and_directory(this_directory)

    #create folder and subfolders for the cropped photos
    cropped_photo_folder_path = crete_folder_and_subfolders(this_directory, folder_directory_dic)
    
    # crop photo function, send current directory , directory of the new folders for cropped photos
    crop_photos(folder_directory_dic, cropped_photo_folder_path )
   


if __name__ == "__main__":
    main()