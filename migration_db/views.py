from django.shortcuts import render
from django.urls import reverse
from django.shortcuts import redirect
from migration_db.models import Project, Node,quote,user,invoice
# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.db.models import Sum, Q
import openpyxl
STATES = ['Vic','Qld','NSW','SA','WA','NT']
def hello(request):
    return  HttpResponse("Hello world")


def login(request):

    return render(request, 'login.html')


def login_result(request):
    context_dict = {}
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['pass_word']
        if user.objects.filter(username=username).filter(password=password).exists():
            request.session['username']=username
            return redirect('index')
        else:
            context_dict['msg']='msg'
            ret_msg=u'Your username or password is not correct.Please log in again'
            return render(request, 'login.html',{'msg': ret_msg})

def register(request):
    return render(request,'register.html')

def register_result(request):
    context_dict = {}
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        if user.objects.filter(username=username).exists():
            context_dict['status'] = 'fail'
        else:
            context_dict['status']='success'
            user.objects.create(username=username, password=password)
        return render(request, 'register_result.html', context_dict)




def import_page(request):
    return render(request, 'import.html')

# def import_project(request):
#     return render()

def chart_page(request):
    return render(request,'allNodesByNode.html')

def state_page(request):
    return render(request,'allNodesByState.html')

def compute_ab(request):
    return render(request,'compute_ab.html')

def index(request):
    if request.session.get("username","") =="":
        return redirect("login")
    return render(request,'index.html')

def filter_page(request,node_name_slug):
    if request.session.get("username","") =="":
        return redirect("login")
    context_dict = {}
    context_dict['node_name'] = node_name_slug
    return render(request,'nodeFilter.html',context_dict)


def chartbynode(request):
    if request.session.get("username","") =="":
        return redirect("login")
    if request.method == 'POST':
        from_date = request.POST['from_user_date']
        to_date = request.POST['to_user_date']
        num_cus_va = None
        subtotal_va = None
        if 'num_cus' in request.POST:
            num_cus_va = request.POST['num_cus']
        if 'subtotal' in request.POST:
            subtotal_va = request.POST['subtotal']
        if Project.objects.filter(pro_date__gte=from_date, pro_date__lte=to_date).exists():
            projects = Project.objects.filter(pro_date__gte=from_date, pro_date__lte=to_date)
        if num_cus_va == 'value1':
            data = {}

            data.setdefault('1', 0)
            data.setdefault('2', 0)
            data.setdefault('3', 0)
            data.setdefault('4', 0)
            data.setdefault('5', 0)

            if projects.filter(node='AWRI'):
                data['1'] += list(projects.filter(node='AWRI').aggregate(Sum('cus_count')).values())[0]
            if projects.filter(node='Murdoch'):
                data['2'] += list(projects.filter(node='Murdoch').aggregate(Sum('cus_count')).values())[0]
            if projects.filter(node='UQ'):
                data['3'] += list(projects.filter(node='UQ').aggregate(Sum('cus_count')).values())[0]
            if projects.filter(node='UM'):
                data['4'] += list(projects.filter(node='UM').aggregate(Sum('cus_count')).values())[0]
            if projects.filter(node='UWA'):
                data['5'] += list(projects.filter(node='UWA').aggregate(Sum('cus_count')).values())[0]
            return render(request, 'allNodesByNode_num_result.html', {'AWRI': data['1'], 'Murdoch': data['2'],'UQ': data['3'],'UM': data['4'], 'UWA':data['5']})
        else:
            data = {}

            data.setdefault('1', 0)
            data.setdefault('2', 0)
            data.setdefault('3', 0)
            data.setdefault('4', 0)
            data.setdefault('5', 0)

            if projects.filter(node='AWRI'):
                data['1'] += list(projects.filter(node='AWRI').aggregate(Sum('subtotal')).values())[0]
            if projects.filter(node='Murdoch'):
                data['2'] += list(projects.filter(node='Murdoch').aggregate(Sum('subtotal')).values())[0]
            if projects.filter(node='UQ'):
                data['3'] += list(projects.filter(node='UQ').aggregate(Sum('subtotal')).values())[0]
            if projects.filter(node='UM'):
                data['4'] += list(projects.filter(node='UM').aggregate(Sum('subtotal')).values())[0]
            if projects.filter(node='UWA'):
                data['5'] += list(projects.filter(node='UWA').aggregate(Sum('subtotal')).values())[0]
            return render(request, 'allNodesByNode_total_result.html',
                          {'AWRI': data['1'], 'Murdoch': data['2'], 'UQ': data['3'], 'UM': data['4'], 'UWA': data['5']})
    # context_dict={}
    # if request.method == 'POST':
    #     from_date = request.POST['from_user_date']
    #     to_date = request.POST['to_user_date']
    #     num_cus_va = None
    #     subtotal_va = None
    #     if 'num_cus' in request.POST:
    #         num_cus_value = request.POST['num_cus']
    #     if 'subtotal' in request.POST:
    #         subtotal_value = request.POST['subtotal']
    #     if num_cus_va == 'num_cus_va':
    #         data = []
    #         Node_choice = ['AWRI', 'Murdoch', 'UQ', 'UM', 'UWA']
    #         if Project.objects.filter(pro_date__gte=from_date, pro_date__lte=to_date).exists():
    #             projects = Project.objects.filter(pro_date__gte=from_date, pro_date__lte=to_date)
    #             for t in Node_choice:
    #
    #                 if projects.filter(node=t).exists():
    #                     data.append(list(projects.filter(node=t).aggregate(Sum('subtotal')).values())[0])
    #                 else:
    #                     data.append(0)
    #         context_dict['subtotal'] = data
    #
    #         return render(request,'allNodesByNode_total_result.html',context_dict)
    #     else:
    #         data = []
    #         Node_choice = ['AWRI', 'Murdoch', 'UQ', 'UM', 'UWA']
    #         if Project.objects.filter(pro_date__gte=from_date, pro_date__lte=to_date).exists():
    #             projects = Project.objects.filter(pro_date__gte=from_date, pro_date__lte=to_date)
    #             for t in Node_choice:
    #
    #                 if projects.filter(node=t).exists():
    #                     data.append(list(projects.filter(node=t).aggregate(Sum('cus_count')).values())[0])
    #                 else:
    #                     data.append(0)
    #         context_dict['cus_count'] = data
    #         return render(request, 'allNodesByNode_num_result.html', context_dict)

def logout(request):
    if request.session.get('username', '') != '':
        del request.session['username']
    return redirect('login')

def filter_result(request,node_name_slug):
    if request.session.get("username","") =="":
        return redirect("login")
    context_dict = {}
    if request.method=='POST':
        from_date = request.POST['from_user_date']
        to_date = request.POST['to_user_date']
        category_value=None
        user1_value=None
        user2_value=None
        state_value=None

        if 'Category' in request.POST:
            category_value = request.POST['Category']
        if 'User_Define1' in request.POST:
            user1_value = request.POST['User_Define1']
        if 'User_Define2' in request.POST:
            user2_value = request.POST['User_Define2']
        if 'State' in request.POST:
            state_value = request.POST['State']
        print request.POST
        print user1_value
        print user2_value
        if state_value == 'va_state':
            data = []

            if Project.objects.filter(pro_date__gte=from_date, pro_date__lte=to_date).exists():
                projects = Project.objects.filter(pro_date__gte=from_date, pro_date__lte=to_date)

                for t in STATES:
                    data.append(t)
                    if projects.filter(state=t).exists():
                        data.append(list(projects.filter(state=t).aggregate(Sum('subtotal')).values())[0])
                        data.append(list(projects.filter(state=t).aggregate(Sum('cus_count')).values())[0])
                       # data.append(projects.filter(state=t).count())
                        data.append(list(projects.filter(state=t).aggregate(Sum('num_sample')).values())[0])
                    else:
                        data.append(0)
                        data.append(0)
                        data.append(0)
                        data.append(0)

                data = [data[x:x + 5] for x in range(0, len(data), 5)]
            else:
                data = [[0, 0, 0, 0, 0]]
            context_dict['State'] = data
        if user2_value == 'va_user_define2':
            data = []
            user2_choice = ['LIF/FOO', 'BIO', 'LIF/MED', 'ENV', 'LIF/AGR', 'LIF', 'PHA']
            if Project.objects.filter(pro_date__gte=from_date, pro_date__lte=to_date).exists():
                projects = Project.objects.filter(pro_date__gte=from_date, pro_date__lte=to_date)

                for t in user2_choice:
                    data.append(t)
                    if projects.filter(user_define1=t).exists():
                        data.append(list(projects.filter(user_define2=t).aggregate(Sum('subtotal')).values())[0])
                        data.append(list(projects.filter(user_define2=t).aggregate(Sum('cus_count')).values())[0])
                        #data.append(projects.filter(user_define2=t).count())
                        data.append(list(projects.filter(user_define2=t).aggregate(Sum('num_sample')).values())[0])
                    else:
                        data.append(0)
                        data.append(0)
                        data.append(0)
                        data.append(0)

                data = [data[x:x + 5] for x in range(0, len(data), 5)]
            else:
                data = [[0, 0, 0, 0, 0]]
            context_dict['User_Define2'] = data
        if user1_value == 'va_user_define1':
            data = []
            user1_choice = ['PRDC', 'UNI', 'CF','CB','CO','CP','POTH']
            if Project.objects.filter(pro_date__gte=from_date, pro_date__lte=to_date).exists():
                projects = Project.objects.filter(pro_date__gte=from_date, pro_date__lte=to_date)

                for t in user1_choice:
                    data.append(t)
                    if projects.filter(user_define1=t).exists():
                        data.append(list(projects.filter(user_define1=t).aggregate(Sum('subtotal')).values())[0])
                        data.append(list(projects.filter(user_define1=t).aggregate(Sum('cus_count')).values())[0])
                        data.append(projects.filter(user_define1=t).count())
                        data.append(list(projects.filter(user_define1=t).aggregate(Sum('num_sample')).values())[0])
                    else:
                        data.append(0)
                        data.append(0)
                        data.append(0)
                        data.append(0)

                data = [data[x:x + 5] for x in range(0, len(data), 5)]
            else:
                data = [[0, 0, 0, 0, 0]]
            context_dict['User_Define1'] = data
        if category_value == 'va_category':
            cates = ['1', '2', '3']
            data = []
            if Project.objects.filter(pro_date__gte=from_date, pro_date__lte=to_date).exists():
                projects = Project.objects.filter(pro_date__gte=from_date, pro_date__lte=to_date)

                for t in cates:
                    data.append(t)
                    if projects.filter(category=t).exists():
                        data.append(list(projects.filter(category=t).aggregate(Sum('subtotal')).values())[0])
                        data.append(list(projects.filter(category=t).aggregate(Sum('cus_count')).values())[0])
                        data.append(projects.filter(category=t).count())
                        data.append(list(projects.filter(category=t).aggregate(Sum('num_sample')).values())[0])
                    else:
                        data.append(0)
                        data.append(0)
                        data.append(0)
                        data.append(0)

                data = [data[x:x + 5] for x in range(0, len(data), 5)]
            else:
                data = [[0, 0, 0, 0, 0]]
            context_dict['Category']=data
    print context_dict
    return render(request, 'nodeFilter_result.html', context_dict)




def filter_state(request):
    if request.session.get("username","") =="":
        return redirect("login")
    context_dict = {}
    data = []
    if request.method == 'POST':
        from_date = request.POST['from_user_date']
        to_date = request.POST['to_user_date']


        if Project.objects.filter(pro_date__gte=from_date, pro_date__lte=to_date).exists():
            projects = Project.objects.filter(pro_date__gte=from_date, pro_date__lte=to_date)

            for t in STATES:
                data.append(t)
                if projects.filter(state=t).exists():
                    data.append(list(projects.filter(state=t).aggregate(Sum('subtotal')).values())[0])
                    data.append(list(projects.filter(state=t).aggregate(Sum('cus_count')).values())[0])
                    # data.append(projects.filter(state=t).count())
                    data.append(list(projects.filter(state=t).aggregate(Sum('num_sample')).values())[0])
                # else:
                #     data.append(0)
                #     data.append(0)
                #     data.append(0)
                #     data.append(0)

            data = [data[x:x + 4] for x in range(0, len(data), 4)]
        else:
            data = [[0, 0, 0, 0, 0]]
        context_dict['State'] = data
        return render(request, 'allNodesByState_result.html', context_dict)


def add(request):
    a=request.GET['a']
    b = request.GET['b']
    a=int(a)
    b=int(b)
    return HttpResponse(str(a+b))

def node(request, node_name_slug):
    if request.session.get("username","") =="":
        return redirect("login")
    context_dict={}
    context_dict['node_name'] = node_name_slug
    projects = Project.objects.filter(node=node_name_slug)
    context_dict['projects'] = projects
    return render(request,'node.html',context_dict)

def projects_list(request,node_name_slug):
    if request.session.get("username","") =="":
        return redirect("login")
    context_dict = {}
    try:
        context_dict['node_name_slug'] = node_name_slug
        node = Node.objects.get(node_abbr=node_name_slug)
        projects = Project.objects.filter(node=node_name_slug)
        context_dict['p'] = projects
        return render(request, 'nodeProTable.html', context_dict)
    except Node.DoesNotExist:
        return render(request, 'nodeProTable.html', context_dict)






def test_projects_list(request):
    if request.session.get("username",None) ==None:
        return HttpResponseRedirect(reverse('login'))
    context_dict = {}
    try:


        p = Project.objects.filter(node='UM')
        context_dict['p'] = p


    except Node.DoesNotExist:
        pass

    return render(request,'nodeProTable.html',context_dict)


def project_detail(request,pro_id):
    if request.session.get("username",None) ==None:
        return HttpResponseRedirect(reverse('login'))
    context_dict={}
    try:
        p = Project.objects.get(pro_id=pro_id)
    except:
        p = None
    context_dict['pro_id']=p.pro_id
    context_dict['p']=p

    return render(request,'project_detail.html',context_dict)


def node_chart(request,node_name_slug):
    print request.session.get('username','no user name')
    if request.session.get('username','') =='':
        return HttpResponseRedirect('login')
    # print request.session.get('username')
    def get_aggregation(node_name_slug):
        res = {}
        res.setdefault('1',0)
        res.setdefault('2',0)
        res.setdefault('3',0)

        projects = Project.objects.filter(node=node_name_slug)

        if projects.filter(category='1'):
            res['1']+=list(projects.filter(category='1').aggregate(Sum('subtotal')).values())[0]
        if projects.filter(category='2') :
            res['2']+=list(projects.filter(category='2').aggregate(Sum('subtotal')).values())[0]
        if projects.filter(category='3') :
            res['3']+=list(projects.filter(category='3').aggregate(Sum('subtotal')).values())[0]
        return res


    data = get_aggregation(node_name_slug)

    return render(request,'nodeIncomeChart.html',{'cat1':data['1'],'cat2':data['2'],'cat3':data['3']})



# quote
# def quote_filter(request):
def quote_page(request):
    if request.session.get("username","") =="":
        return redirect("login")
    return render(request, 'quote.html')


def quote_grant(request):
    if request.session.get("username","") =="":
        return redirect("login")
    return render(request, 'quote_grant.html')

def quote_status(request):
    if request.session.get("username","") =="":
        return redirect("login")
    return render(request, 'quote_status.html')

def quote_company(request):
    if request.session.get("username","") =="":
        return redirect("login")
    return render(request, 'quote_company.html')

def quote_grant_result(request):
    if request.session.get("username","") =="":
        return redirect("login")
    context_dict = {}
    if request.method == 'POST':
        from_date = request.POST['from_user_date']
        to_date = request.POST['to_user_date']
        print from_date
        arc_va = None
        n_va = None
        others_va=None
        if 'ARC' in request.POST:
            arc_va = request.POST['ARC']
        if 'N' in request.POST:
            n_va = request.POST['N']
        if 'Others' in request.POST:
            others_va = request.POST['Others']
        if quote.objects.filter(quote_date__gte=from_date, quote_date__lte=to_date).exists():
            quotes = quote.objects.filter(quote_date__gte=from_date, quote_date__lte=to_date)

            if arc_va == 'arc_va':
                ARC_qu=quotes.filter(grant_not='ARC')

                context_dict['ARC'] = ARC_qu
            if others_va == 'others_va':
                Others_q =quotes.filter(grant_not='Null')
                context_dict['others'] = Others_q
            if n_va == 'n_va':
                N_q = quotes.filter(grant_not='N')
                context_dict['N'] = N_q
            arc_sum=quotes.filter(grant_not='ARC').aggregate(Sum('quote_value')).values()[0]
            print arc_sum
            context_dict['ARC_Sum']=arc_sum
            n_sum = quotes.filter(grant_not='N').aggregate(Sum('quote_value')).values()[0]
            print n_sum
            context_dict['N_Sum'] = n_sum
            others_sum = quotes.filter(grant_not='Null').aggregate(Sum('quote_value')).values()[0]
            print others_sum
            context_dict['others_Sum'] =others_sum
            return render(request, 'quote_grant_result.html', context_dict)


def quote_grant_detail(request,quote_id):
    if request.session.get("username","") =="":
        return redirect("login")
    context_dict={}
    try:
        q = quote.objects.get(quote_id=quote_id)
    except:
        q = None
    context_dict['quote_id']=q.quote_id
    context_dict['q']=q

    return render(request,'quote_grant_detail.html',context_dict)



def quote_status_detail(request,quote_id):
    if request.session.get("username","") =="":
        return redirect("login")
    context_dict={}
    try:
        q = quote.objects.get(quote_id=quote_id)
    except:
        q = None
    context_dict['quote_id']=q.quote_id
    context_dict['q_status']=q

    return render(request,'quote_status_detail.html',context_dict)

def quote_status_result(request):
    if request.session.get("username","") =="":
        return redirect("login")
    context_dict = {}
    if request.method == 'POST':
        from_date = request.POST['from_user_date']
        to_date = request.POST['to_user_date']
        print from_date
        accept_va = None
        invoice_va = None

        if 'accept' in request.POST:
            accept_va = request.POST['accept']
        if 'invoice' in request.POST:
            invoice_va= request.POST['invoice']

        if quote.objects.filter(quote_date__gte=from_date, quote_date__lte=to_date).exists():
            quotes = quote.objects.filter(quote_date__gte=from_date, quote_date__lte=to_date)

            if accept_va == 'accept_va' and  invoice_va=='invoice_va':
                q_status = quotes.filter(accept='Y').filter(invoiced_not='Y')
                Status_Sum = quotes.filter(accept='Y').filter(invoiced_not='Y').aggregate(Sum('quote_value')).values()[0]
                context_dict['q_status'] = q_status
                context_dict['Status_Sum'] = Status_Sum
            if accept_va == 'accept_va' and invoice_va != 'invoice_va':
                q_status = quotes.filter(accept='Y').filter(invoiced_not='Null')
                Status_Sum = quotes.filter(accept='Y').filter(invoiced_not='Null').aggregate(Sum('quote_value')).values()[0]
                context_dict['q_status'] = q_status
                context_dict['Status_Sum'] = Status_Sum
            if accept_va != 'accept_va' and invoice_va == 'invoice_va':
                q_status = quotes.filter(accept='Null').filter(invoiced_not = 'Y')
                Status_Sum = quotes.filter(accept='Null').filter(invoiced_not = 'Y').aggregate(Sum('quote_value')).values()[0]
                context_dict['q_status'] = q_status
                context_dict['Status_Sum'] = Status_Sum
            if accept_va != 'accept_va' and invoice_va != 'invoice_va':
                q_status = quotes.filter(accept='Null').filter(invoiced_not = 'Null')
                Status_Sum = quotes.filter(accept='Null').filter(invoiced_not='Null').aggregate(Sum('quote_value')).values()[0]
                context_dict['q_status'] = q_status
                context_dict['Status_Sum'] = Status_Sum

            return render(request, 'quote_status_result.html', context_dict)

def quote_company_result(request):
    if request.session.get("username","") =="":
        return redirect("login")
    context_dict = {}
    if request.method == 'POST':

        company = request.POST['company']
        quotes = quote.objects.filter(company=company)
        context_dict['q_company']=quotes
        return render(request, 'quote_company_result.html', context_dict)

def quote_company_detail(request,quote_id):
    if request.session.get("username","") =="":
        return redirect("login")
    context_dict={}
    try:
        q = quote.objects.get(quote_id=quote_id)
    except:
        q = None
    context_dict['quote_id']=q.quote_id
    context_dict['q_company']=q

    return render(request,'quote_company_detail.html',context_dict)

def invoice_page(request):
    return render(request, 'invoice.html')

def search(request):
    return render(request, 'search.html')

def invoice_result(request):
    if request.session.get("username","") =="":
        return redirect("login")
    context_dict = {}
    if request.method=='POST':
        from_date = request.POST['from_user_date']
        to_date = request.POST['to_user_date']

        paid_va=None
        unpaid_va=None


        if 'paid' in request.POST:
            paid_va = request.POST['paid']
        if 'unpaid' in request.POST:
            unpaid_va = request.POST['unpaid']

        print paid_va
        print unpaid_va
        if paid_va == 'paid_va':


            if invoice.objects.filter(invoice_date__gte=from_date, invoice_date__lte=to_date).exists():
                invoices = invoice.objects.filter(invoice_date__gte=from_date, invoice_date__lte=to_date)
                paid=invoices.filter(paid='Y')

            context_dict['paid'] = paid
        if unpaid_va == 'unpaid_va':


            if invoice.objects.filter(invoice_date__gte=from_date, invoice_date__lte=to_date).exists():
                invoices = invoice.objects.filter(invoice_date__gte=from_date, invoice_date__lte=to_date)
                unpaid = invoices.filter(paid='N')

            context_dict['unpaid'] = unpaid
        return render(request, 'invoice_result.html', context_dict)


def invoice_detail(request,invoice_id):
    if request.session.get("username",None) ==None:
        return HttpResponseRedirect(reverse('login'))
    context_dict={}
    try:
        p = invoice.objects.get(invoice_id=invoice_id)
    except:
        p = None
    context_dict['invoice_id']=invoice_id
    context_dict['i']=p

    return render(request,'invoice_detail.html',context_dict)

def search_result(request):
    if request.session.get("username",None) ==None:
        return HttpResponseRedirect(reverse('login'))
    context_dict = {}
    if request.method == 'POST':
        from_date = request.POST['from_user_date']
        to_date = request.POST['to_user_date']
        if Project.objects.filter(pro_date__gte=from_date, pro_date__lte=to_date).exists():
            projects = Project.objects.filter(pro_date__gte=from_date, pro_date__lte=to_date)
            person = request.POST['person']
            organisation = request.POST['organisation']
            service = request.POST['service']
            description = request.POST['description']
            instrument = request.POST['instrument']
            pros=projects.all()
            if person!='':
                pros=pros.filter(person=person)
            if organisation!='':
                pros=pros.filter(organization=organisation)
            if service!='':
                pros=pros.filter(service=service)
            if description!='':
                pros=pros.filter(project_name=description)
            if instrument!='':
                pros=pros.filter(instrument=instrument)
            print len(pros)
            personF=list(filter(lambda x:x.person==person if person!='' else True,pros))
            # s1=projects.filter(project_name="*")
            # s2=projects.filter(organization=organisation)
            # s3=projects.filter(service=service)
            # s4=projects.filter(instrument=instrument)
            # s5=projects.filter(person=person)

            context_dict['s'] =pros

        return render(request, 'search_result.html', context_dict)

def search_detail(request,search_id):

    if request.session.get("username", None) == None:
        return HttpResponseRedirect(reverse('login'))
    context_dict = {}
    try:
        p = Project.objects.get(pro_id=search_id)
    except:
        p = None
    context_dict['pro_id'] = search_id
    context_dict['s'] = p

    return render(request, 'search_detail.html', context_dict)