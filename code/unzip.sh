input_dir=$1

if [ -z "$input_dir" ]; then
    echo "Usage: $0 <input_dir>"
    exit 1
fi

# unzip all zip file in subdirectories and save in the its current directory with .tsv extension
for file in $(find $input_dir -name "*.zip"); do
    echo "Unzipping $file"
    unzip $file -d $(dirname $file)
    echo "Done"
done
