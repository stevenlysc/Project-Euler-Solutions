# /bin/sh

cd ~/Documents/ProjectEuler
rm -r Result
mkdir Result

for f in `ls` 
do
	if [ $f != "runit.sh" ] && [ $f != "Result" ]; then
		chmod +x $f
		./$f >> Result/$f.txt
		echo $f finished.
		echo 
	fi
done
