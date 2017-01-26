from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
import random

def randomNum(min,max):
    return random.randrange(min,max+1)

# Create your views here.
def index(request):
    print "*****************INDEX"

    if 'gold' not in request.session:
        print "**************FIRST IF"
        request.session['gold'] = 0
    if request.session['gold'] < 0:
        print "**************SECOND IF"
        request.session['gold'] = 0

    if 'activity_log' not in request.session:
        print "**************Third IF"
        request.session['activity_log'] = []
    print "*************END OF INDEX"
    return render(request, 'ninjaGold/index.html')

def reset(request):
    print "****************RESET"
    request.session['gold'] = 0
    request.session['activity_log'].append("\nYou burned all your money")
    return redirect(reverse('ninjagold:my_index'))

def clear_log(request):
    request.session['activity_log']= []
    return redirect(reverse('my_index'))

def process(request,building):


    if request.method == 'POST':
        if building == 'farm':
            print "\nfarm clicked\n"
            gold = randomNum(10,20)
            request.session['gold'] += gold
            print "\nFound %s gold"%(gold)
            print "current gold:",request.session['gold'],"\n"
            request.session['activity_log'].append("\nCurrent gold: {}".format(request.session['gold']))
            request.session['activity_log'].append("\nFound %s gold at the Farm"%(gold))
            return redirect(reverse('my_index'))
        elif building == 'cave':
            print "\cave clicked\n"
            gold = randomNum(5,10)
            request.session['gold'] += gold
            print "\nFound %s gold"%(gold)
            print "current gold:",request.session['gold'],"\n"
            request.session['activity_log'].append("\nCurrent gold: {}".format(request.session['gold']))
            request.session['activity_log'].append("\nFound %s gold at the Cave"%(gold))
            return redirect(reverse('my_index'))
        elif building == 'house':
            print "\nfarm clicked\n"
            gold = randomNum(2,5)
            request.session['gold'] += gold
            print "\nFound %s gold"%(gold)
            print "current gold:",request.session['gold'],"\n"
            request.session['activity_log'].append("\nCurrent gold: {}".format(request.session['gold']))
            request.session['activity_log'].append("\nFound %s gold at the House"%(gold))
            return redirect(reverse('my_index'))
        elif building == 'casino':
            print "\ncasino clicked\n"
            gold = randomNum(-50,50)
            if request.session['gold'] <= 0:
                print "You don't have any money to gamble"
                request.session['activity_log'].append("\nCurrent gold: {}".format(request.session['gold']))
                request.session['activity_log'].append("\nYou don't have any money to gamble")
                return redirect (reverse('my_index'))
            request.session['gold'] += gold
            if gold == 0:
                print "You broke even at the casino"
            elif gold > 0:
                print "\nFound %s gold"%(gold)
                request.session['activity_log'].append("\nCurrent gold: {}".format(request.session['gold']))
                request.session['activity_log'].append("\nWon %s gold at the Casino"%(gold))
            else:
                print "\nLost %s gold"%(gold)
                print "current gold:",request.session['gold'],"\n"
                request.session['activity_log'].append("\nCurrent gold: {}".format(request.session['gold']))
                request.session['activity_log'].append(['\nLost %s gold at the Casino'%(gold*(-1)),'color:red'])
            return redirect(reverse('my_index'))
    return redirect(reverse('my_index'))
