awk '{print $2}' uv.txt | sort | uniq | wc -l
cat uv.txt | grep '2015-08-24' |awk -F ' ' '{print $2}' | sort -u | wc -l
