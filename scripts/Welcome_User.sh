#! bin/sh

# Add this to the .rc file of your shell

echo -e "Hello \033[1;32m$USER!!\033[0m What have you been upto?"
RANDOM=$$
ch=$(($RANDOM % 10))
curr_time=`date +%H`

if [ $curr_time -gt 12 ]
then
    case $ch in
        0) echo "Don't let insecurity ruin the beauty you were born with."
        ;;
        1) echo "To live is the rarest thing in the world. Most people exist, that is all."
        ;;
        2) echo "Shoot for the moon. Even if you miss, you will land among the stars."
        ;;
        3) echo "Your value doesn't decrease based on someone's inablility to see your worth."
        ;;
        4) echo "If you can dream it, you can do it."
        ;;
        5) echo "Don't let the opinions of others define you."
        ;;
        6) echo "You were given this life, because you were strong enough to live it."
        ;;
        7) echo "Work hard in silence. Let the success make the noise!"
        ;;
        8) echo "Winners are not people who never fail, but people who never quit."
        ;;
        9) echo "See the invisible, Believe the incredible, Achieve the impossible."
        ;;
    esac
else
    case $ch in
        0) echo "The universe is made up of protons, neutron, electrons and morons!"
        ;;
        1) echo "Where there is a shell, there is a way!"
        ;;
        2) echo "Eat. Sleep. Code. Repeat"
        ;;
        3) echo "How do you generate a random string? Put a web designer in front of Vim and tell her/him to save and exit!"
        ;;
        4) echo "There is no place like ~"
        ;;
        5) echo "What did Linux say to the Windows partition? Go fsck youself!"
        ;;
        6) echo "You are so fat, the recursive function computing your mass causes a stack overflow!"
        ;;
        7) echo "There is no place like 127.0.0.1"
        ;;
        8) echo "cout << C > C++;   //huh! false"
        ;;
        9) echo "Go to sleep dear!"
        ;;
    esac
fi 
