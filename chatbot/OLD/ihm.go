package main

import (
	"bytes"
	"encoding/json"
	"fmt"
	"io/ioutil"
	"net/http"
	"fyne.io/fyne/v2"
	"fyne.io/fyne/v2/app"
	"fyne.io/fyne/v2/container"
	"fyne.io/fyne/v2/widget"
)

const serverURL = "http://localhost:5000/chat" // Remplacez par l'URL de votre serveur

type Request struct {
	Message string `json:"message"`
}

type Response struct {
	Reply string `json:"reply"`
}

func sendRequest(message string) (string, error) {
	requestData := Request{Message: message}
	jsonData, err := json.Marshal(requestData)
	if err != nil {
		return "", err
	}

	resp, err := http.Post(serverURL, "application/json", bytes.NewBuffer(jsonData))
	if err != nil {
		return "", err
	}
	defer resp.Body.Close()

	body, err := ioutil.ReadAll(resp.Body)
	if err != nil {
		return "", err
	}

	var responseData Response
	if err := json.Unmarshal(body, &responseData); err != nil {
		return "", err
	}

	return responseData.Reply, nil
}

func main() {
	myApp := app.New()
	myWindow := myApp.NewWindow("Chatbot")
	myWindow.Resize(fyne.NewSize(400, 300))

	input := widget.NewEntry()
	input.SetPlaceHolder("Tapez votre question...")
	
	output := widget.NewLabel("Réponse ici...")
	
	button := widget.NewButton("Envoyer", func() {
		if input.Text == "" {
			output.SetText("Veuillez entrer une question.")
			return
		}
		response, err := sendRequest(input.Text)
		if err != nil {
			output.SetText("Erreur: " + err.Error())
		} else {
			output.SetText(response)
		}
	})

	myWindow.SetContent(container.NewVBox(input, button, output))
	myWindow.ShowAndRun()
}
