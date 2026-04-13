<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">

    <xsl:template match="/">
        <html>
            <head>
                <title>Inventario de Juegos</title>
                <style>
                    table { border-collapse: collapse; width: 50%; }
                    th, td { border: 1px solid black; padding: 8px; text-align: left; }
                    th { background-color: #f2f2f2; }
                </style>
            </head>
            <body>
                <h2>Lista de Videojuegos</h2>
                <table>
                    <tr>
                        <th>Título</th>
                        <th>Consola</th>
                        <th>Precio</th>
                    </tr>
                    <xsl:for-each select="tienda/videojuego">
                        <xsl:sort select="precio" data-type="number" order="descending" />
                        <tr>
                            <td>
                                <xsl:value-of select="titulo" />
                            </td>
                            <td>
                                <xsl:value-of select="@consola" />
                            </td>
                            <td>
                                <xsl:value-of select="precio" />
                                <xsl:value-of select="precio/@moneda" />
                            </td>
                        </tr>
                    </xsl:for-each>
                </table>
            </body>
        </html>
    </xsl:template>

</xsl:stylesheet>