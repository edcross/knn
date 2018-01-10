#!/bin/bash
#seq=1
#cont=10
#until [ $cont -lt 1 ];
#do
#echo $cont

for f in $(cat test.txt); do
echo $f
	
python creadorDeDoc.py $f

	NPROC=$(($NPROC+1))
    if [ "$NPROC" -ge 3 ]; then
        wait
        NPROC=0
    fi
done

 #let cont=cont-1 
 #done

echo "finish process"


