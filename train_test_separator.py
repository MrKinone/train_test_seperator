import random
import glob
import shutil
import os
import argparse

def train_test_seperator(img_dir, train_test_dir, ratio=0.8):
    """
    :param img_dir: Enter the path to the folder where the images are located
    :param train_test_dir: Enter the path of the train and test folder
            if the folder is not created it will be created automatically
    :param ratio: train/test ratio it must be between [0,1]
            if write 1 it's copy all files in train folder
    :return: none
    """

    img_list = []

    for filename in glob.glob(img_dir + '/*.jpg'):
        img_list.append(filename)

    train_dir = train_test_dir + "\\train"
    test_dir = train_test_dir + "\\test"

    folder_check(train_dir)
    folder_check(test_dir)

    print(" % i images found" % len(img_list))
    train_num = round(len(img_list) * ratio)

    for i in range(train_num):
        file_number = random.randint(0, len(img_list) - 1)

        shutil.copy(img_list[file_number], train_dir)

        xml_file = img_list[file_number][:-4] + ".xml"
        txt_file = img_list[file_number][:-4] + ".txt"

        if os.path.isfile(xml_file):
            shutil.copy(xml_file, train_dir)
        elif os.path.isfile(txt_file):
            shutil.copy(txt_file, train_dir)

        img_list.remove(img_list[file_number])

    for i in range(len(img_list)):

        file_number = random.randint(0, len(img_list) - 1)

        shutil.copy(img_list[file_number], test_dir)

        xml_file = img_list[file_number][:-4] + ".xml"
        txt_file = img_list[file_number][:-4] + ".txt"
        if os.path.isfile(xml_file):
            shutil.copy(xml_file, test_dir)
        elif os.path.isfile(txt_file):
            shutil.copy(txt_file, test_dir)

        img_list.remove(img_list[file_number])
    return


def folder_check(DIR):
    """
    :param DIR: type the folder you want to check
                if the folder is not created it will be created automatically
    :return: none
    """
    if not os.path.isdir(DIR):
        os.mkdir(DIR)
        print("Directory '% s' created" % DIR)
    return


if __name__ == '__main__':
    arg_parse = argparse.ArgumentParser(description='this script separates your images as train and test')
    arg_parse.add_argument('-i', '--image_directory', type=str,  required=True, help="Enter the path to the folder where the images are located")
    arg_parse.add_argument('-t', '--train_test_directory', type=str, required=True,
                           help="Enter the path of the train and test folder if the folder is not created it will be created automatically")
    arg_parse.add_argument('-r', '--ratio', type=float, required=False,
                        help="train/test ratio it must be between [0,1]. Default=0.8")
    args = arg_parse.parse_args()
    train_test_seperator(img_dir=args.image_directory, train_test_dir=args.train_test_directory, ratio=args.ratio)
