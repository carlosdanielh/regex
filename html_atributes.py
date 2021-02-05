'''
Charlie's second assignment was given by the Professor as soon as he submitted the first one. Professor asked Charlie to create a list of all the attributes of every tag found in HTML pages.

<p>This is a paragraph</p>  
The above HTML string has p as its tag but no attributes.

<a href="http://www.quackit.com/html/tutorial/html_links.cfm">Example Link</a>
This string has a as a tag and href as an attribute.

Input Format

The first line contains N, the number of lines in the HTML fragment. This is followed by lines from a valid HTML document or fragment.

Constraints

Number of characters in the test fragments <= 10000 characters. Characters will
be restricted to ASCII. Fragments for the tests will be picked up from Wikipedia.
Attributes are all lowercase alphabets.

Output Format

Each tag must be separated by a newline arranged in lexicographic order
Each attribute noted for a given tag must be arranged next to a tag in
 lexicographic order.

The output will be of the format

tag-1:attribute-1,attribute-2,attribute-3....
tag-2:attribute-1,attribute-2,attribute-3....
tag-3:attribute-1,attribute-2,attribute-3....
...
tag-n:attribute-1,attribute-2,attribute-3....
Where tag-1 is lexicographically smaller than tag-2 and attribute-1 is
 lexicographically smaller than attribute-2

Sample Input:1

2
<p><a href="http://www.quackit.com/html/tutorial/html_links.cfm">Example
Link</a></p>
<div class="more-info">
<a href="http://www.quackit.com/html/examples/html_links_examples.cfm">
More Link Examples...</a></div>

Sample Output:1

a:href
div:class
p:
###############################################################################
Sample Input:2

9
<li style="-moz-float-edge: content-box">... that <a href="/wiki/Orval_Overall" title="Orval Overall">Orval Overall</a> <i>(pictured)</i> is the only <b><a href="/wiki/List_of_Major_League_Baseball_pitchers_who_have_struck_out_four_batters_in_one_inning" title="List of Major League Baseball pitchers who have struck out four batters in one inning">Major League Baseball player to strike out four batters in one inning</a></b> in the <a href="/wiki/World_Series" title="World Series">World Series</a>?</li>
<li style="-moz-float-edge: content-box">... that the three cities of the <b><a href="/wiki/West_Triangle_Economic_Zone" title="West Triangle Economic Zone">West Triangle Economic Zone</a></b> contribute 40% of Western China's GDP?</li>
<li style="-moz-float-edge: content-box">... that <i><a href="/wiki/Kismet_(1943_film)" title="Kismet (1943 film)">Kismet</a></i>, directed by <b><a href="/wiki/Gyan_Mukherjee" title="Gyan Mukherjee">Gyan Mukherjee</a></b>, ran at the <a href="/wiki/Roxy_Cinema_(Kolkata)" title="Roxy Cinema (Kolkata)">Roxy, Kolkata</a>, for 3 years and 8 months?</li>
<li style="-moz-float-edge: content-box">... that <a href="/wiki/Vauix_Carter" title="Vauix Carter">Vauix Carter</a> both coached and played for the <b><a href="/wiki/1882_Navy_Midshipmen_football_team" title="1882 Navy Midshipmen football team">1882 Navy Midshipmen football team</a></b>?</li>
<li style="-moz-float-edge: content-box">... that <a href="/wiki/Zhu_Chenhao" title="Zhu Chenhao">Zhu Chenhao</a> was sentenced to <a href="/wiki/Slow_slicing" title="Slow slicing">slow slicing</a> for leading the <b><a href="/wiki/Prince_of_Ning_rebellion" title="Prince of Ning rebellion">Prince of Ning rebellion</a></b> against the <a href="/wiki/Ming_Dynasty" title="Ming Dynasty">Ming Dynasty</a> <a href="/wiki/Zhengde_Emperor" title="Zhengde Emperor">emperor Zhengde</a>?</li>
<li style="-moz-float-edge: content-box">... that <b><a href="/wiki/Mirza_Adeeb" title="Mirza Adeeb">Mirza Adeeb</a></b> was a prominent modern Pakistani <a href="/wiki/Urdu" title="Urdu">Urdu</a> playwright whose later work focuses on social problems and daily life?</li>
<li style="-moz-float-edge: content-box">... that in <i><b><a href="/wiki/La%C3%9Ft_uns_sorgen,_la%C3%9Ft_uns_wachen,_BWV_213" title="Lat uns sorgen, lat uns wachen, BWV 213">Die Wahl des Herkules</a></b></i>, Hercules must choose between the good cop and the bad cop?<br style="clear:both;" />
<div style="text-align: right;" class="noprint"><b><a href="/wiki/Wikipedia:Recent_additions" title="Wikipedia:Recent additions">Archive</a></b>  <b><a href="/wiki/Wikipedia:Your_first_article" title="Wikipedia:Your first article">Start a new article</a></b>  <b><a href="/wiki/Template_talk:Did_you_know" title="Template talk:Did you know">Nominate an article</a></b></div>
</li>
Sample Output:2

a:href,title
b:
br:style
div:class,style
i:
li:style
'''
import re
import pyperclip

def order_atribute(html):
    regex = re.compile(r'(<[\w\s]+=|[\w]+=[\'\"]+|<\w+>)')
    find = regex.findall(html)
    print(find)
    print('--------------------------------')
    concat = ''
    position_to_copy = 0
    first_occurrance = True
    for index, element in enumerate(find):
        # import pdb; pdb.set_trace()
        if index != 0:
            if '<' not in find[index]:

                if first_occurrance:
                    position_to_copy = index - 1
                    first_occurrance = False
                concat += ' ' + find[index]
                find[index] = ''
            else:
                find[position_to_copy] += concat
                concat = ''
                first_occurrance = True
    
    if concat != '':
        find[position_to_copy] += concat

    print(find)
    find = list(set(find))
    find = (list(filter(lambda x: x, find)))
    print('-------------------------------------')
    print(find)
    for index, element in enumerate(find):
        find[index] = element.replace('<', ' ')\
                             .replace('="', ' ')\
                             .replace('>', ' ')\
                             .replace('=', ' ')\
                             .replace('\'', ' ')\
                             .replace('\"', ' ')\
                             .strip()
    print('-------------------------------------')
    print(find)
    for index, element in enumerate(find):

        if element.count(' ') >= 1:
            b = element.split()

        if element.count(' ') == 0:
            find[index] += ':'
        elif element.count(' ') == 1:
            find[index] = b[0] + ':' + b[1]
        else:
            find[index] = b[0] + ':' + ','.join(sorted(b[1:]))

    lista = sorted(find)

    new_lista = []
    result = ''
    regex = re.compile(r'\w+:')
    for element in lista:
        cabezal = regex.search(element)
        cabezal = cabezal.group()

        for elemento in lista:
            if cabezal == regex.search(elemento).group() and cabezal not in result:
                new_lista.append(elemento)
        if len(new_lista) != 0:
            result += max(new_lista, key=len) + ' '
            new_lista.clear()

    return '\n'.join(sorted(result.split()))

htt='''
49
<div class="portal" role="navigation" id='p-lang'>
<h3>Languages</h3>
<div class="body">
<ul>
<li class="interwiki-simple"><a href="//simple.wikipedia.org/wiki/" title="" lang="simple" hreflang="simple">Simple English</a></li>
<li class="interwiki-ar"><a href="//ar.wikipedia.org/wiki/" title="" lang="ar" hreflang="ar"></a></li>
<li class="interwiki-id"><a href="//id.wikipedia.org/wiki/" title="" lang="id" hreflang="id">Bahasa Indonesia</a></li>
<li class="interwiki-ms"><a href="//ms.wikipedia.org/wiki/" title="" lang="ms" hreflang="ms">Bahasa Melayu</a></li>
<li class="interwiki-bg"><a href="//bg.wikipedia.org/wiki/" title="" lang="bg" hreflang="bg"></a></li>
<li class="interwiki-ca"><a href="//ca.wikipedia.org/wiki/" title="" lang="ca" hreflang="ca">Catal</a></li>
<li class="interwiki-cs"><a href="//cs.wikipedia.org/wiki/" title="" lang="cs" hreflang="cs">esky</a></li>
<li class="interwiki-da"><a href="//da.wikipedia.org/wiki/" title="" lang="da" hreflang="da"><b>Dansk</b></a></li>
<li class="interwiki-de{-truncated-}
'''
html='''
13
<div class="portal" role="navigation" id='p-navigation'>
<h3>Navigation</h3>
<div class="body">
<ul>
<li id="n-mainpage-description"><a href="/wiki/Main_Page" title="Visit the 
main page [z]" accesskey="z">Main page</a></li>
<li id="n-contents"><a href="/wiki/Portal:Contents" title="Guides to browsing
 Wikipedia">Contents</a></li>
<li id="n-featuredcontent"><a href="/wiki/Portal:Featured_content"
 title="Featured content  the best of Wikipedia">Featured content</a></li>
<li id="n-currentevents"><a href="/wiki/Portal:Current_events"
 title="Find background information on current events">Current events</a></li>
<li id="n-randompage"><a href="/wiki/Special:Random" 
title="Load a random article [x]" accesskey="x">Random article</a></li>
<li id="n-sitesupport">
<a href="//donate.wikimedia.org/wiki/Special:FundraiserRedirector?
=donate&amp;utm_medium=sidebar&amp;utm_campaign=C13_en.wikipedia.org&amp;
uselang=en" title="Support us">Donate to Wikipedia</a></li>
</ul>
</div>
</div>
'''

'''
a:accesskey,href,title
div:class,id,role
h3:
li:id
ul:
'''

html2 ='''
2
<p><a href="http://www.quackit.com/html/tutorial/html_links.cfm">Example Link</a></p>
<div class="more-info"><a href="http://www.quackit.com/html/examples/html_links_examples.cfm">More Link Examples...</a></div>'''

# lista = order_atribute(html2)
# new_lista = []
# result = ''
# regex = re.compile(r'\w+:')
# for element in lista:
#     cabezal = regex.search(element)
#     cabezal = cabezal.group()

#     for elemento in lista:
#         if cabezal in elemento and cabezal not in result:
#             new_lista.append(elemento)
#     if len(new_lista) != 0:
#         result += max(new_lista, key=len) + ' '
#         new_lista.clear()

# print('\n'.join(sorted(result.split())))
c='''
7
<center>
<div class="noresize" style="height: 242px; width: 600px; "><map name="ImageMap_1_971996215" id="ImageMap_1_971996215">
<area href="/wiki/File:Pardalotus_punctatus_female_with_nesting_material_-_Risdon_Brook.jpg" shape="rect" coords="3,3,297,238" alt="Female" title="Female" />
<area href="/wiki/File:Pardalotus_punctatus_male_with_nesting_material_-_Risdon_Brook.jpg" shape="rect" coords="302,2,597,238" alt="Male" title="Male" /></map><img alt="Pair of Spotted Pardalotes" src="//upload.wikimedia.org/wikipedia/commons/thumb/5/5b/Female_and_male_Pardalotus_punctatus.jpg/600px-Female_and_male_Pardalotus_punctatus.jpg" width="600" height="242" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/5/5b/Female_and_male_Pardalotus_punctatus.jpg/900px-Female_and_male_Pardalotus_punctatus.jpg 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/5/5b/Female_and_male_Pardalotus_punctatus.jpg/1200px-Female_and_male_Pardalotus_punctatus.jpg 2x" usemap="#ImageMap_1_971996215" />
<div style="margin-left: 0px; marg{-truncated-}
'''

d='''
7
<ul>
<li style="-moz-float-edge: content-box">Former Italian Prime Minister <a href="/wiki/Silvio_Berlusconi" title="Silvio Berlusconi">Silvio Berlusconi</a> <i>(pictured)</i> is <b><a href="/wiki/Silvio_Berlusconi_underage_prostitution_charges" title="Silvio Berlusconi underage prostitution charges">found guilty</a></b> of paying for sex with an underage prostitute.</li>
<li style="-moz-float-edge: content-box">In sports car racing, the <b><a href="/wiki/2013_24_Hours_of_Le_Mans" title="2013 24 Hours of Le Mans">24 Hours of Le Mans</a></b>, won by <a href="/wiki/Tom_Kristensen" title="Tom Kristensen">Tom Kristensen</a>, <a href="/wiki/Allan_McNish" title="Allan McNish">Allan McNish</a> and <a href="/wiki/Lo%C3%AFc_Duval" title="Loc Duval">Loc Duval</a>, is marred by the death of <b><a href="/wiki/Allan_Simonsen_(racing_driver)" title="Allan Simonsen (racing driver)">Allan Simonsen</a></b>.</li>
<li style="-moz-float-edge: content-box"><b><a href="/wiki/2013_Alberta_floods" title="2013 Alberta floods">Flood{-truncated-}'''
v = pyperclip.paste()

print(order_atribute(v))