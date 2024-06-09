folders=(combined-outliers hunger-outliers social-outliers work-outliers)
root=../dataset/pol

for folder in "${folders[@]}"; do
    echo "Cleaning $folder"
    # rm -rf $root/$folder/*.zip
    # remove subdirectories
    for subfolder in $(find $root/$folder -mindepth 1 -maxdepth 1 -type d); do
        echo "Removing $subfolder"
        rm -rf $subfolder
    done
    echo "Done"
done
