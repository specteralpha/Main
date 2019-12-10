#! /bin/bash

clear

echo "***START***"

continuE="y"

while [ $continuE == "y" ]

do

	continuE1="y"

	clear

	echo ""

	echo "	***********************"

	echo "	+++ AVALIBLE MENU'S +++"

	echo "	***********************"

	echo ""

	echo "	1. Full Applications"

	echo "	2. Enables/Disables"

	echo "	3. RECON"

	echo "	4. ATTACk"

	echo "	5. CRACK"

	echo "	6. EXIT"

	echo ""

	read -p "	Please Select an Option: " menu

	if [ $menu == 1 ] #----Full Applications
	then

		while [ $continuE1 == "y" ]
		do

			clear

			echo ""

			echo "	*******************************"

			echo "	+++ MENU: Full Applications +++"

			echo "	*******************************"

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

			echo "	*****************************"

			echo "	+++ MENU: Enables/Disables +++"

			echo "	*****************************"

			echo ""

			echo "	Avalible Option'S"

			echo ""

			echo "	1. Enable Monitor Mode"

			echo "	2. Enable Monitor Mode -KILL"

			echo "	3. Disable Monitor Mode"

			echo "	4. Return to Main Menu"

			echo ""

			read -p "	Please Select an Option: " option

			if [ $option == 1 ] #----Enable Monitor Mode
			then

				clear

				echo ""

				echo "	***************************"
		
				echo "	+++ Enable Monitor Mode +++"

				echo "	***************************"
		
				echo ""

				read -p "	What Wireless Interface (wlan0): " interface

				interface=${interface:-wlan0}

				sudo airmon-ng start $interface

				echo "	(1/2) COMPLETE"
				
				echo ""

				iwconfig $interface"mon"
				
				echo ""

				echo "	(2/2) COMPLETE"
				
				echo ""

				read -p "	Press ENTER to Continue." null

			elif [ $option == 2 ] #--Enable Monitor Mode -KILL
			then

				clear

				echo ""

				echo "	*********************************"
		
				echo "	+++ Enable Monitor Mode -KILL +++"

				echo "	*********************************"
		
				echo ""

				read -p "	What Wireless Interface (wlan0): " interface

				interface=${interface:-wlan0}

				sudo ifconfig $interface down

				echo "	(1/4) COMPLETE"

				sudo airmon-ng check kill

				echo "	(2/4) COMPLETE"

				sudo ifconfig $interface up

				echo "	(3/4) COMPLETE"

				sudo airmon-ng start $interface

				echo "	(4/4) COMPLETE"

				echo ""

				iwconfig $interface"mon"

				echo ""

				read -p "	Press ENTER to Continue." null

			elif [ $option == 3 ] #--Disable Monitor Mode
			then

				clear

				echo ""

				echo "	****************************"
		
				echo "	+++ Disable Monitor Mode +++"

				echo "	****************************"
				
				echo ""

				read -p "	What Wireless Interface in Monitor Mode (wlan0mon): " interface

				interface=${interface:-wlan0mon}

				sudo airmon-ng stop $interface

				echo "	(1/1) COMPLETE"

				echo ""

				read -p "	Press ENTER to Continue." null

			elif [ $option == 4 ] #--Return to Main Menu
			then

				continuE1="n"

			else #Invalid

				clear

				echo ""

				echo "	**************************************************************"

				echo "	--- INVALID OPTION, PRESS ENTER TO RETURN TO PREVIOUS MENU ---"

				echo "	**************************************************************"

				read null

			fi

		done

	elif [ $menu == 3 ] #--RECON
	then

		while [ $continuE1 == "y" ]
		do

			clear

			echo ""

			echo "	*******************"

			echo "	+++ MENU: RECON +++"

			echo "	*******************"

			echo ""

			echo "	Avalible Option'S"

			echo ""

			echo "	1. WiFi Sniffer"

			echo "	2. Targeted WiFi Sniffer"

			echo "	3. Port Scanner"

			echo "	4. Return to Main Menu"

			echo ""

			read -p "	Please Select an Option: " option

			if [ $option == 1 ] #----WiFi Sniffer
			then
	
				clear
		
				echo ""

				echo "	*******************"
		
				echo "	RECON WiFi Sniffer"

				echo "	*******************"

				echo ""
		
				echo ""

				read -p "	What Wireless Interface in Monitor Mode (i.e. wlan0mon): " interface

				interface=${interface:-wlan0mon}

				airodump-ng $interface

				echo "	(1/1) COMPLETE"
				
				echo ""

				echo "	Press ENTER to Continue."

				read null

			elif [ $option == 2 ] #--Targeted WiFi Sniffer
			then

				clear

				echo ""

				echo "	*****************************"
		
				echo "	RECON Targeted WiFi Sniffer"

				echo "	*****************************"
		
				echo ""

				read -p "	What Wireless Interface in Monitor Mode (i.e. wlan0mon): " interface

				interface=${interface:-wlan0mon}

				read -p "	What MAC Address: " address

				read -p "	What Channel: " channel

				read -p "	Save name?: " save

				if [ $save > 0 ]
				then

					airodump-ng --bssid $address --channel $channel --write $save $interface

				else

					airodump-ng --bssid $address --channel $channel $interface

				fi

				echo "	(1/1) COMPLETE"
				
				echo ""

				echo "	Press ENTER to Continue."

				read null

			elif [ $option == 3 ] #--Port Scanner
			then

				clear

				echo ""

				echo "	*******************"
		
				echo "	RECON Port Scanner"

				echo "	*******************"
		
				echo ""

				read -p "	Enter the Starting IP Address: " firstIP

				read -p "	Enter the Last Octet of the Last IP Address: " lastoc

				read -p "	Enter the Port Number to Scan for: " port

				nmap -sT $firstIP-$lastoc -P $port >/dev/null -oG MySQLscan

				echo ""

				echo "	(1/3) COMPLETE"
				
				echo ""

				cat MySQLscan | grep open > MySQLscan2

				echo ""

				echo "	(2/3) COMPLETE"
				
				echo ""

				cat MySQLscan2

				echo "	(3/3) COMPLETE"
				
				echo ""

				echo "	Press ENTER to Continue."

				read null

			elif [ $option == 4 ] #--Return to Main Menu
			then

				continuE1="n"

			else #Invalid

				clear

				echo ""

				echo "	**************************************************************"

				echo "	--- INVALID OPTION, PRESS ENTER TO RETURN TO PREVIOUS MENU ---"

				echo "	**************************************************************"

				read null

			fi

		done

	elif [ $menu == 4 ] #--ATTACK
	then

		while [ $continuE1 == "y" ]
		do

			clear

			echo ""

			echo "	************"

			echo "	MENU: ATTACK"

			echo "	************"

			echo ""

			echo "	Avalible Option'S"

			echo ""

			echo "	1. Deauthorization"

			echo "	2. Return to Main Menu"

			echo ""

			read -p "	Please Select an Option: " option

			if [ $option == 1 ] #----Deauthorization
			then

				clear
  
				echo ""

				echo "	**********************"
		
				echo "	ATTACk Deauthorization"

				echo "	**********************"
		
				echo ""
   
				read -p "	What Wireless Interface in Monitor Mode (i.e. wlan0mon): " interface

				read -p "What AP MAC Address: " address

				read -p "What Client MAC Address: " caddress

				read -p "How Many Packets: " packets

				aireplay-ng --deauth $packets -a $aaddress -c $caddress $interface

				echo "	(1/1) COMPLETE"
				
				echo ""

				echo "	Press ENTER to Continue."

				read null

			elif [ $option == 2 ] #--
			then

				continuE1="n"

			elif [ $option == 3 ] #--Return to Main Menu
			then

				continuE1="n"

			else #Invalid

				clear

				echo ""

				echo "	**************************************************************"

				echo "	--- INVALID OPTION, PRESS ENTER TO RETURN TO PREVIOUS MENU ---"

				echo "	**************************************************************"

				read null

			fi

		done

	elif [ $menu == 5 ] #--CRACK
	then

		while [ $continuE1 == "y" ]
		do

			clear

			echo ""

			echo "	***********"

			echo "	MENU: CRACK"

			echo "	***********"

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

				echo "	**************************************************************"

				echo "	--- INVALID OPTION, PRESS ENTER TO RETURN TO PREVIOUS MENU ---"

				echo "	**************************************************************"

				read null

			fi

		done


	elif [ $menu == 6 ] #--EXIT
	then

		continuE="n"
	
	else #Invalid

		clear

		echo ""

		echo "	**************************************************************"

		echo "	--- INVALID OPTION, PRESS ENTER TO RETURN TO THE MAIN MENU ---"

		echo "	**************************************************************"

		read null

	fi

done

clear

echo "***DONE***"

exit 0
