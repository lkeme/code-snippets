# CURL测试流量
i=1
while [ $((i++)) -le 16 ]
do
wget -O /dev/null http://hlsmgspvod.miguvideo.com/depository_sjq/asset/zhengshi/5102/191/875/5102191875/media/5102191875_5004454776_91.mp4
done