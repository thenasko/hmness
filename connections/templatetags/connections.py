from django import template

register = template.Library()

@register.simple_tag(takes_context=True)
def connections_init(context, connection_end, self_name='', be_verb='is', can_edit=False):
    context['connections_connection_end'] = connection_end
    context['connections_be_verb'] = be_verb
    context['connections_can_edit'] = bool(can_edit)
    
    if self_name == '':
        context['connections_self_name'] = connection_end.name
    else:
        context['connections_self_name'] = self_name

    c_in_only, c_out_only, c_in_out = connection_end.connections_pack

    context['connections_in_only'] = c_in_only
    context['connections_out_only'] = c_out_only
    context['connections_in_out'] = c_in_out
    context['connections_in_count'] = len(c_in_only) + len(c_in_out)
    context['connections_out_count'] = len(c_out_only) + len(c_in_out)

    return ''

@register.inclusion_tag("connections_list.html", takes_context=True)
def connections_list(context):
    return context
