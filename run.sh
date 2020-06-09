# bash run.sh <subject_name> <webcam url> <http ip> <conda env name> <init temp>
# example: bash run.sh zyt http://192.168.0.108:8080/video 192.168.0.102 py37 35.0
SUBJECT_NAME=$1
WEBCAM_URL=$2
HTTP_IP=$3
CONDA_ENV_NAME=$4
TEMP=$5
tmux new-session -s incubator -d "source deactivate; conda activate $CONDA_ENV_NAME; cd ~/Desktop/Baby-Incubator; python get_pulse_temp.py --subject $SUBJECT_NAME --url $WEBCAM_URL --init_temp $TEMP"
tmux new-window -t incubator:1 "source deactivate; conda activate $CONDA_ENV_NAME; cd ~/Desktop/Baby-Incubator; python connect_app.py $HTTP_IP"
tmux attach -t incubator
