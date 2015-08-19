# http://www.amazon.com/Drive-Medical-Rollator-Removable-Support/product-reviews/B005S1CHKC/ref=cm_cr_pr_btm_link_163?ie=UTF8&showViewpoints=1&sortBy=recent&reviewerType=all_reviews&formatType=all_formats&filterByStar=all_stars&pageNumber=163

import time
import re
from retrieveurl import graburlcontent

amazon = ["http://www.amazon.com/Drive-Medical-Rollator-Removable-Support/product-reviews/B005S1CHKC/ref=cm_cr_pr_btm_link_163?ie=UTF8&showViewpoints=1&sortBy=recent&reviewerType=all_reviews&formatType=all_formats&filterByStar=all_stars&pageNumber=163"]


####################### Setting the Stage (methods) #######################


def grab_reviewer_name(pagetext):
    reviewername = re.findall('pdp\?ie=UTF8">(.+)</a></span><sp', pagetext)
    return reviewername

def grab_star_rating(pagetext):
    starrating = re.findall('="a-icon-alt">(.+)</span></i', pagetext)
    return starrating

def grab_reviews(pagetext):
    reviews = re.findall('<span class="a-size-base review-text">(.+)</span></div><div', pagetext)
    return reviews    

all_ratings = []

####################### Execution part #######################
for i in amazon:
    try:
        page_contents = graburlcontent(i)
        #print(page_contents)
        
       
        
        reviewer_names = grab_reviewer_name(page_contents)
        star_ratings = grab_star_rating(page_contents)[2:]
        reviews = grab_reviews(page_contents)
        
        x = 0
        for i in range(x, len(reviews)):
            print('Name: ', reviewer_names[x].replace('&amp;','and'), '\n')
            print('Stars they gave to the product: ', star_ratings[x], '\n')
            print('Review: ', reviews[x].replace('<br /><br />',' '),'\n')
            print('\n'*2)
            
            x += 1
            
            

    except:
        print("can't print for some reason, check the control flow in zipsx")
        continue

        print('\n')
        

        #time.sleep(10)
