Vim�UnDo� �	��v_r��j���|�]�=�c���-�7B   6                                   Z%    _�                             ����                                                                                                                                                                                                                                                                                                                                                             Z      �                 class Institution(models.Model):5�_�                            ����                                                                                                                                                                                                                                                                                                                                                             Z      �                 5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             Z      �                5    nom = models.CharField(max_length=100, null=True)5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             Z      �                (    source = models.TextField(null=True)5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             Z      �                )    article = models.TextField(null=True)5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             Z!     �                6    type = models.CharField(max_length=100, null=True)5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             Z!     �                6    pays = models.CharField(max_length=100, null=True)5�_�      	                     ����                                                                                                                                                                                                                                                                                                                                                             Z!     �                7    where = models.CharField(max_length=100, null=True)5�_�      
           	           ����                                                                                                                                                                                                                                                                                                                                                             Z!     �                 5�_�   	              
          ����                                                                                                                                                                                                                                                                                                                                                             Z!     �                    def __str__(self):5�_�   
                        ����                                                                                                                                                                                                                                                                                                                                                             Z"     �                        return self.nom5�_�                            ����                                                                                                                                                                                                                                                                                                                                                             Z"     �                 5�_�                            ����                                                                                                                                                                                                                                                                                                                                                             Z#     �                 5�_�                             ����                                                                                                                                                                                                                                                                                                                                                             Z$    �                 5��