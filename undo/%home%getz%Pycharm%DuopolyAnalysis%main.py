Vim�UnDo� ���hQ�t�)�R��ih=ï!$��d   �                  $       $   $   $    Z�],    _�                             ����                                                                                                                                                                                                                                                                                                                                                             Z�YE     �         ?    5�_�                            ����                                                                                                                                                                                                                                                                                                                                                             Z�YG     �                 5�_�                            ����                                                                                                                                                                                                                                                                                                                                                             Z�YG     �         @       �         ?    5�_�                            ����                                                                                                                                                                                                                                                                                                                                                             Z�YM     �                from django.core5�_�                    	        ����                                                                                                                                                                                                                                                                                                                                                             Z�YR    �   	      ?    5�_�                            ����                                                                                                                                                                                                                                                                                                                                                             Z�Y]     �         @      1from django.core.wsgi import get_wsgi_application5�_�                            ����                                                                                                                                                                                                                                                                                                                                                             Z�Y_     �         @    �         @    5�_�      	                      ����                                                                                                                                                                                                                                                                                                                                                             Z�Ya     �         A      $application = get_wsgi_application()5�_�      
           	           ����                                                                                                                                                                                                                                                                                                                                                             Z�Yb     �         A    �         A    5�_�   	              
           ����                                                                                                                                                                                                                                                                                                                                                             Z�Yd     �                # Ensure settings are read5�_�   
                         ����                                                                                                                                                                                                                                                                                                                                                             Z�Yd    �                 5�_�                            ����                                                                                                                                                                                                                                                                                                                                                             Z�Yl     �      	   @      Rfrom game.models import Users, Players, Room, Round, RoundComposition, FirmProfits5�_�                            ����                                                                                                                                                                                                                                                                                                                                                             Z�Yn     �         @    �         @    5�_�                            ����                                                                                                                                                                                                                                                                                                                                                             Z�Yp     �         A    5�_�                            ����                                                                                                                                                                                                                                                                                                                                                             Z�Yq     �         B    5�_�                    
        ����                                                                                                                                                                                                                                                                                                                                                             Z�Yr     �   	   
          ## Your application specific imports5�_�                    
        ����                                                                                                                                                                                                                                                                                                                                                             Z�Yr    �   	   
          k5�_�                    7   C    ����                                                                                                                                                                                                                                                                                                                                                             Z�Y�     �   5   7          %        print("Total profit", profit)�   6   8   A      U        print("{} TO PAY: 1$ + {:.2f} $ BONUS".format(mt_id, profit*conversion_rate))5�_�                    7   E    ����                                                                                                                                                                                                                                                                                                                                                             Z�Y�    �   5   7          %        print("Total profit", profit)�   6   8   A      V        print("{} TO PAY: 1$ + {:.2f} $ BONUS".format(mt_id, profit *conversion_rate))5�_�                    A   
    ����                                                                                                                                                                                                                                                                                                                                                             Z�Y�     �   A                  �   A            5�_�                    C       ����                                                                                                                                                                                                                                                                                                                                                             Z�Y�     �   C   F   E          �   C   E   D    5�_�                            ����                                                                                                                                                                                                                                                                                                                                                             Z�Y�     �         G       �         F    5�_�                    F       ����                                                                                                                                                                                                                                                                                                                                                             Z�Y�     �   E   G   G          if sys.argv[5�_�                    F   !    ����                                                                                                                                                                                                                                                                                                                                                             Z�Y�     �   F   I   H              �   F   H   G    5�_�                    G       ����                                                                                                                                                                                                                                                                                                                                                             Z�Y�     �   E   G          "    if "compensation" in sys.argv:�   F   H   I              get_compensation5�_�                       %    ����                                                                                                                                                                                                                                                                                                                                                             Z�Y�     �         J          �         I    5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             Z�Z     �                    Players.objects.get(tamree5�_�                            ����                                                                                                                                                                                                                                                                                                                                                             Z�Z�     �         K       �         J    5�_�                            ����                                                                                                                                                                                                                                                                                                                                                             Z�Z�     �                from game.models import Tamere5�_�                            ����                                                                                                                                                                                                                                                                                                                                                             Z�Z�    �                    5�_�                     
        ����                                                                                                                                                                                                                                                                                                                                                             Z�Z�    �   	   
           5�_�      !                      ����                                                                                                                                                                                                                                                                                                                                                             Z�Z�     �         I      %    conversion_rate = 0.5 * 10 **(-3)5�_�       "           !          ����                                                                                                                                                                                                                                                                                                                                      C           v       Z�Z�     �      D   I   2       # Application logic   1    user = Users.objects.get(mechanical_id=mt_id)       M    print("Looking for MT {} ({})".format(user.mechanical_id, user.username))       5    p = Players.objects.get(player_id=user.player_id)           ,    rm = Room.objects.get(room_id=p.room_id)           if rm.state == "end":   "        ending_t = rm.ending_t - 1   #        print("ending_t", ending_t)       6        rds = Round.objects.filter(room_id=rm.room_id)       #        round_id_and_agent_ids = []               for rd in rds:       e            rc = RoundComposition.objects.filter(round_id=rd.round_id, player_id=p.player_id).first()               if rc is not None:   I                round_id_and_agent_ids.append((rd.round_id, rc.agent_id))               profit = 0       9        for round_id, agent_id in round_id_and_agent_ids:       ?            # print("round_id", round_id, "agent_id", agent_id)       `            pr = FirmProfits.objects.get(agent_id=agent_id, t=ending_t, round_id=round_id).value                   profit += pr       J            state = Round.objects.get(round_id=round_id).state  # pve, pvp   :            print("Profit round {}: {}".format(state, pr))       %        print("Total profit", profit)   W        print("{} TO PAY: 1$ + {:.2f} $ BONUS".format(mt_id, profit * conversion_rate))       	    else:   0        print("Room did not reach ending state")           if user.deserter:   .            print("{} DESERTER".format(mt_id))               else:   0            print("{} TO PAY: 1$".format(mt_id))           print()    5�_�   !   #           "           ����                                                                                                                                                                                                                                                                                                                                      C           v       Z�Z�     �         J       �         I    5�_�   "   $           #           ����                                                                                                                                                                                                                                                                                                                                      E           v       Z�Z�     �                def 5�_�   #               $           ����                                                                                                                                                                                                                                                                                                                                      D           v       Z�]+     �               J   # Django specific settings   	import os   
import sys   1from django.core.wsgi import get_wsgi_application       Rfrom game.models import Users, Players, Room, Round, RoundComposition, FirmProfits       ;os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")   $application = get_wsgi_application()               def get_compensation(mt_ids):       %    conversion_rate = 0.5 * 10 **(-3)           for mt_id in mt_ids:               # Application logic   5        user = Users.objects.get(mechanical_id=mt_id)       Q        print("Looking for MT {} ({})".format(user.mechanical_id, user.username))       9        p = Players.objects.get(player_id=user.player_id)           0        rm = Room.objects.get(room_id=p.room_id)               if rm.state == "end":   &            ending_t = rm.ending_t - 1   '            print("ending_t", ending_t)       :            rds = Round.objects.filter(room_id=rm.room_id)       '            round_id_and_agent_ids = []                   for rd in rds:       i                rc = RoundComposition.objects.filter(round_id=rd.round_id, player_id=p.player_id).first()   "                if rc is not None:   M                    round_id_and_agent_ids.append((rd.round_id, rc.agent_id))                   profit = 0       =            for round_id, agent_id in round_id_and_agent_ids:       C                # print("round_id", round_id, "agent_id", agent_id)       d                pr = FirmProfits.objects.get(agent_id=agent_id, t=ending_t, round_id=round_id).value                       profit += pr       N                state = Round.objects.get(round_id=round_id).state  # pve, pvp   >                print("Profit round {}: {}".format(state, pr))       )            print("Total profit", profit)   [            print("{} TO PAY: 1$ + {:.2f} $ BONUS".format(mt_id, profit * conversion_rate))               else:   4            print("Room did not reach ending state")               if user.deserter:   2                print("{} DESERTER".format(mt_id))                   else:   4                print("{} TO PAY: 1$".format(mt_id))               print()       if __name__ == '__main__':       "    if "compensation" in sys.argv:   &        get_compensation(sys.argv[2:])        5��