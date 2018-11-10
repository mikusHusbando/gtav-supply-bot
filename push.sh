if (( $# == 1))
then
	git add *
	git commit -m "$1" -S
	git push origin master
else
	echo "pass commit message!"
fi
