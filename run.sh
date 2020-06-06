# bash run.sh <subject_name> <webcam url> <http ip>
# example: bash run.sh zyt http://192.168.0.108:8080/video 192.168.0.102
SUBJECT_NAME=$1
WEBCAM_URL=$2
HTTP_IP=$3
tmux new-session -s incubator -d "source deactivate; conda activate bioexp; which python; cd ~/Desktop/Baby-Incubator; python get_pulse_temp.py --subject $SUBJECT_NAME --url $WEBCAM_URL"
tmux new-window -t incubator:1 "source deactivate; conda activate bioexp; which python; cd ~/Desktop/Baby-Incubator; python connect_app.py $HTTP_IP"
tmux attach -t incubator
