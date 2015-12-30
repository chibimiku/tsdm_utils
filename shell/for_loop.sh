#copy.sh

for ((i=1;i<=24;i++));do
if [ $i -le 9 ] ;then
  echo we got: 0$i;
else
  echo we got: $i;
fi
done