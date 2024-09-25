library(shiny)
library(plotly)

# Load the dataset
data <- reactive({
  if (!is.null(input$file)) {
    read.csv(input$file$datapath)
  } else {
    mtcars
  }
})

ui <- fluidPage(
  fileInput("file", "Upload Data", accept = c("csv", "xlsx")),
  selectInput("cols", "Select Columns", choices = names(data())),
  plotlyOutput("plot")
)

server <- function(input, output) {
  output$plot <- renderPlotly({
    plot_ly(data()[, input$cols], layout = list(title = "Scatter Plot"))
  })
}

shinyApp(ui = ui, server = server)