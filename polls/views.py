from django.shortcuts import render, redirect
import pandas as pd
import pickle

def index_func(request):
    res = 0
    if request.method == 'POST':
        name = request.POST['name']
        NumDots = request.POST['NumDots']
        PathLevel = request.POST['PathLevel']
        NumDash = request.POST['NumDash']
        NumSensitiveWords= request.POST['NumSensitiveWords']
        PctExtHyperlinks = request.POST['PctExtHyperlinks']
        PctExtResourceUrls= request.POST['PctExtResourceUrls']
        InsecureForms = request.POST['InsecureForms']
        tooLong = request.POST['PctNullSelfRedirectHyperlinks']
        freq = request.POST['FrequentDomainNameMismatch']
        SubmitInfoToEmail = request.POST['SubmitInfoToEmail']
        IframeOrFrame = request.POST['IframeOrFrame']

        if name != "":
            df = pd.DataFrame(columns=['NumDots','PathLevel','NumDash','NumSensitiveWords',
                                       'PctExtHyperlinks','PctExtResourceUrls','InsecureForms',
                                       'PctNullSelfRedirectHyperlinks','FrequentDomainNameMismatch',
                                       'SubmitInfoToEmail','IframeOrFrame'])

            df2 = pd.DataFrame({
                'NumDots': float(NumDots) if NumDots else 0.0,
                'PathLevel': float(PathLevel) if PathLevel else 0.0,
                'NumDash': float(NumDash) if NumDash else 0.0,
                'NumSensitiveWords': float(NumSensitiveWords) if NumSensitiveWords else 0.0,
                'PctExtHyperlinks': float(PctExtHyperlinks) if PctExtHyperlinks else 0.0,
                'PctExtResourceUrls': float(PctExtResourceUrls) if PctExtResourceUrls else 0.0,
                'InsecureForms': float(InsecureForms) if InsecureForms.isdigit() else 0.0,
                'PctNullSelfRedirectHyperlinks': float(tooLong) if tooLong else 0.0,
                'FrequentDomainNameMismatch': float(freq) if freq.isdigit() else 0.0,
                'SubmitInfoToEmail': float(SubmitInfoToEmail.lower() == 'yes') if SubmitInfoToEmail else 0.0,
                'IframeOrFrame': float(IframeOrFrame.lower() == 'yes') if IframeOrFrame else 0.0,
            }, index=[0])

            df = pd.concat([df, df2], ignore_index=True)

            # Load the model from disk
            filename1 = 'polls/Phishing.pickle'
            loaded_model = pickle.load(open(filename1, 'rb'))
            res = loaded_model.predict(df)
            
            # If the model result is 1, set res to True; otherwise, set it to False
            res = bool(res[0])

            print(res)

        else:
            return redirect('homepage')
    else:
        pass

    return render(request, "index.html", {'response': res})
