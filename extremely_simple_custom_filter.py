#custom filter that will capatilze the message or passed string contents

from djano import template

register = template.library()

@register.filter()
def captatilze(value):
    return "".join(word.upper() for word in list(value) )


<html>
  <head> <title>
  This is my Title!
  </title></head>
  <body>
    <div>
      <h1> {{message | capatilize }}  </h1>
    </div>
  </body>
</html>
