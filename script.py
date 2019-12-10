#! /bin/bash

clear

echo "***START***"

continuE="y"

while [ $continuE == "y" ]

do

	continuE1="y"

	clear

	echo ""
	echo "	+++AVALIBLE MENU'S+++"
	echo ""
	echo "	1. Full Applications"
	echo "	2. Enables/Disables"
	echo "	3. RECON"
	echo "	4. ATTACk"
	echo "	5. EXIT"
	echo ""
	read -p "	Please Select an Option: " menu

	if [ $menu == 1 ] #----Full Applications
	then

		while [ $continuE1 == "y" ]
		do

			clear

			echo ""
			echo "	MENU: Full Applications"
			echo ""
			echo "	Avalible Option'S"
			echo ""
			echo "	1."
			echo "	2. Return to Main Menu"
			echo ""
			read -p "	Please Select an Option: " option

			if [ $option == 1 ] #
			then

				echo "test"

			elif [ $option == 2 ] #Return to Main Menu
			then

				continuE1="n"

			else #Invalid

				clear

				echo ""

				echo "************************************************************"

				echo "---INVALID OPTION, PRESS ENTER TO RETURN TO PREVIOUS MENU---"

				echo "************************************************************"

				read null

			fi

		done

	elif [ $menu == 2 ] #--Enables/Disables
	then

		while [ $continuE1 == "y" ]
		do

			clear

			echo ""
			echo "	MENU: Enables/Disables"
			echo ""
			echo "	Avalible Option'S"
			echo ""
			echo "	1. Enable Monitor Mode"
			echo "	2. Enable Monitor Mode -KILL"
			echo "	3. Disable Monitor Mode"
			echo "	4. Return to Main Menu"
			echo ""
			read -p "	Please Select an Option: " option

			read option

			if [ $option == 1 ] #----Enable Monitor Mode
			then

				clear

				echo ""
		
				echo "Enable Monitor Mode"
		
				echo ""

				read -p "What Wireless Interface (wlan0): " interface

				interface=${interface:-wlan0}

				sudo airmon-ng start $interface

				echo "(1/2) COMPLETE"

				iwconfig $interface"mon"

				echo "(2/2) COMPLETE"

			elif [ $option == 2 ] #--Enable Monitor Mode -KILL
			then

				clear

				echo ""
		
				echo "Enable Monitor Mode -KILL"
		
				echo ""

				read -p "What Wireless Interface (wlan0): " interface

				interface=${interface:-wlan0}

				sudo ifconfig $interface down

				echo "(1/4) COMPLETE"

				sudo airmon-ng check kill

				echo "(2/4) COMPLETE"

				sudo ifconfig $interface up

				echo "(3/4) COMPLETE"

				sudo airmon-ng start $interface

				echo "(4/4) COMPLETE"

				echo ""

				iwconfig $interface"mon"

				echo ""

				echo "Press ENTER to Continue."

				read null

			elif [ $option == 3 ] #--Disable Monitor Mode
			then

				clear

				echo ""
		
				echo "Disable Monitor Mode"
		
				echo ""

				read -p "What Wireless Interface in Monitor Mode (wlan0mon): " interface

				interface=${interface:-wlan0mon}

				sudo airmon-ng stop $interface

				echo "(1/1) COMPLETE"

				echo ""

				echo "Press ENTER to Continue."

				read null

				echo "(1/1) COMPLETE"

			elif [ $option == 4 ] #--Return to Main Menu
			then

				continuE1="n"

			else #Invalid

				clear

				echo ""

				echo "************************************************************"

				echo "---INVALID OPTION, PRESS ENTER TO RETURN TO PREVIOUS MENU---"

				echo "************************************************************"

				read null

			fi

		done

	elif [ $menu == 3 ] #--RECON
	then

		while [ $continuE1 == "y" ]
		do

			clear

			echo ""
			echo "	MENU: RECON"
			echo ""
			echo "	Avalible Option'S"
			echo ""
			echo "	1."
			echo "	2. Return to Main Menu"
			echo ""
			read -p "	Please Select an Option: " option

			if [ $option == 1 ] #----
			then

				echo "test"

			elif [ $option == 2 ] #--Return to Main Menu
			then

				continuE1="n"

			else #Invalid

				clear

				echo ""

				echo "************************************************************"

				echo "---INVALID OPTION, PRESS ENTER TO RETURN TO PREVIOUS MENU---"

				echo "************************************************************"

				read null

			fi

		done

	elif [ $menu == 4 ] #--ATTACK
	then

		while [ $continuE1 == "y" ]
		do

			clear

			echo ""
			echo "	MENU: ATTACK"
			echo ""
			echo "	Avalible Option'S"
			echo ""
			echo "	1."
			echo "	2. Return to Main Menu"
			echo ""
			read -p "	Please Select an Option: " option

			if [ $option == 1 ] #----
			then

				echo "test"

			elif [ $option == 2 ] #--Return to Main Menu
			then

				continuE1="n"

			else #Invalid

				clear

				echo ""

				echo "************************************************************"

				echo "---INVALID OPTION, PRESS ENTER TO RETURN TO PREVIOUS MENU---"

				echo "************************************************************"

				read null

			fi

		done

	elif [ $menu == 5 ] #--EXIT
	then

		continuE="n"
	
	else #Invalid

		clear

		echo ""

		echo "************************************************************"

		echo "---INVALID OPTION, PRESS ENTER TO RETURN TO THE MAIN MENU---"

		echo "************************************************************"

		read null

	fi

done

clear

echo "***DONE***"

exit 0
