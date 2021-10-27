from django.db import models

# Create your models here.
class sport(models.Model):
    sportname = models.CharField(max_length=30)
    sportdesc = models.CharField(max_length=600 , null= True , blank=True)
    created_at = models.DateTimeField(auto_created=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    


    def __str__(self):
        return str(self.sportname)

class team(models.Model):
    teamname = models.CharField(max_length=30)
    teamdesc = models.CharField(max_length=600, null= True , blank=True)
    sport = models.ForeignKey(sport , on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_created=True)
    updated_at = models.DateTimeField(auto_now_add= True)

    class Meta:
        unique_together = ('teamname', 'sport',)
    
    def __str__(self):
        return str(self.teamname)

class match(models.Model):
    matchdesc = models.CharField(max_length=800)
    sport = models.ForeignKey(sport, on_delete=models.CASCADE)

    start = models.DateTimeField(blank=True , null=True)

    matchtype = models.CharField(max_length=40 , blank = True , null = True)

    team1 = models.ForeignKey(team , related_name="team1" , on_delete=models.CASCADE)
    team2 = models.ForeignKey(team , related_name="team2" , on_delete=models.CASCADE)
    venue = models.CharField(max_length=50 , blank = True , null = True)

    def __str__(self):
        return str( str(self.team1) + ' vs ' + str(self.team2) + ' ( ' + str(self.matchdesc) + ' )')

class player(models.Model):
    

    id = models.AutoField(primary_key=True)
    playername = models.CharField(max_length=50)
    playerdesc = models.CharField(max_length=300)

    picture = models.ImageField(default = 'default.png' , upload_to = "product_pictures" , blank = True)

    sport = models.ForeignKey(sport , on_delete=models.CASCADE)
    team = models.ForeignKey(team , on_delete=models.CASCADE)

    

    age = models.IntegerField(blank = True , null=True)

    position = models.CharField(max_length=20 , default = 'batsman' ,blank = True , null=True)
    position_order = models.IntegerField(default = 1 , blank = True , null=True)
    inmatch = models.ManyToManyField( match, related_name='inmatch' , blank=True)

    created_at = models.DateTimeField(auto_created=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.playername)







